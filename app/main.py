import os
import json
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# --- Configurações da API do BookStack ---
# As variáveis de ambiente são lidas do docker-compose.yml
BOOKSTACK_API_URL = os.getenv("BOOKSTACK_API_URL")
API_TOKEN_ID = os.getenv("BOOKSTACK_TOKEN_ID")
API_TOKEN_SECRET = os.getenv("BOOKSTACK_TOKEN_SECRET")

if not all([BOOKSTACK_API_URL, API_TOKEN_ID, API_TOKEN_SECRET]):
    raise EnvironmentError("As variáveis de ambiente BOOKSTACK_API_URL, BOOKSTACK_TOKEN_ID e BOOKSTACK_TOKEN_SECRET devem ser definidas.")

# Cabeçalhos de autenticação
AUTH_HEADERS = {
    "Authorization": f"Token {API_TOKEN_ID}:{API_TOKEN_SECRET}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

app = FastAPI(
    title="BookStack API Manager",
    description="Serviço FastAPI para gerenciar chamadas à API do BookStack."
)

# --- Modelos Pydantic para Requisições ---
class PageCreate(BaseModel):
    book_id: int
    name: str
    content: str # Conteúdo da página em Markdown

# --- Funções de Interação com a API do BookStack ---

def fetch_bookstack_data(endpoint: str):
    """Função genérica para fazer requisições GET à API do BookStack."""
    url = f"{BOOKSTACK_API_URL}{endpoint}"
    try:
        response = requests.get(url, headers=AUTH_HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        if response is not None:
            print(f"Resposta do BookStack: {response.text}")
        raise HTTPException(status_code=response.status_code if response is not None else 500, 
                            detail=f"Erro ao comunicar com o BookStack: {e}")

def post_bookstack_data(endpoint: str, payload: dict):
    """Função genérica para fazer requisições POST à API do BookStack."""
    url = f"{BOOKSTACK_API_URL}{endpoint}"
    try:
        # A API do BookStack para páginas aceita 'html' ou 'markdown' no corpo
        # Usaremos 'html' para o conteúdo, que aceita Markdown
        data_to_send = json.dumps(payload)
        
        response = requests.post(url, headers=AUTH_HEADERS, data=data_to_send)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar dados para {url}: {e}")
        if response is not None:
            print(f"Resposta do BookStack: {response.text}")
        raise HTTPException(status_code=response.status_code if response is not None else 500, 
                            detail=f"Erro ao criar recurso no BookStack: {e}")

# --- Endpoints do FastAPI ---

@app.get("/", tags=["Status"])
def read_root():
    """Verifica se o serviço está online."""
    return {"message": "BookStack API Manager está online."}

@app.get("/books", tags=["BookStack"])
def list_books():
    """Lista todos os livros existentes no BookStack."""
    # O endpoint para listar livros é /books
    data = fetch_bookstack_data("/books")
    return data.get('data', [])

@app.post("/pages", tags=["BookStack"])
def create_page(page_data: PageCreate):
    """Adiciona uma nova página a um livro específico."""
    
    # Prepara o payload para a API do BookStack
    bookstack_payload = {
        "book_id": page_data.book_id,
        "name": page_data.name,
        "html": page_data.content # O campo 'html' aceita conteúdo em Markdown
    }
    
    # O endpoint para criar páginas é /pages
    new_page = post_bookstack_data("/pages", bookstack_payload)
    
    return {
        "message": "Página criada com sucesso",
        "page_id": new_page.get('id'),
        "page_url": new_page.get('url')
    }

# Você pode adicionar mais endpoints aqui, como:
# @app.get("/books/{book_id}/pages") para listar páginas de um livro
# @app.get("/pages/{page_id}") para obter detalhes de uma página
# @app.put("/pages/{page_id}") para atualizar uma página
# @app.delete("/pages/{page_id}") para deletar uma página