# Use uma imagem base Python
FROM python:3.11-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para o diretório app/
# Note que o Dockerfile está na raiz e o código está em ./app/
COPY app/ ./app/

# O comando de execução é definido no docker-compose.yml
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]