# Guia Passo a Passo: Servidor Wiki para Gestão do Conhecimento com Docker Compose

Este guia detalhado apresenta o processo de configuração de um servidor wiki para gestão do conhecimento utilizando **Wiki.js** [1], uma plataforma moderna e poderosa, empacotada em containers Docker e orquestrada com Docker Compose.

O uso de containers garante um ambiente isolado, portátil e de fácil manutenção para a sua base de conhecimento.

## 1. Escolha da Plataforma: Wiki.js

O Wiki.js foi escolhido por ser uma solução *open source* com as seguintes vantagens para gestão do conhecimento:

| Característica | Descrição |
| :--- | :--- |
| **Tecnologia Moderna** | Construído em Node.js, oferecendo alta performance. |
| **Editores Flexíveis** | Suporte a Markdown, HTML e um editor visual (WYSIWYG). |
| **Gestão de Conteúdo** | Controle de versão, pesquisa poderosa e organização hierárquica. |
| **Suporte a Docker** | Imagem oficial e documentação clara para uso com Docker Compose. |

## 2. Pré-requisitos

Para seguir este guia, você deve ter os seguintes softwares instalados em seu sistema operacional (Linux, macOS ou Windows):

1.  **Docker:** A plataforma de containerização.
2.  **Docker Compose:** Ferramenta para definir e executar aplicações multi-container Docker.

## 3. Configuração do Projeto

O projeto será composto por dois arquivos principais: `docker-compose.yml` (definição dos serviços) e `.env` (variáveis de ambiente, como senhas).

### Passo 3.1: Criar o Diretório do Projeto

Crie um novo diretório para o seu projeto e navegue até ele:

```bash
mkdir wiki-server
cd wiki-server
```

### Passo 3.2: Criar o Arquivo de Variáveis de Ambiente (`.env`)

O arquivo `.env` armazenará as senhas e outras configurações sensíveis, mantendo-as fora do arquivo `docker-compose.yml` para maior segurança.

Crie o arquivo `.env` com o seguinte conteúdo:

```ini
# Variáveis de Ambiente para o Docker Compose

# Senha do usuário do banco de dados PostgreSQL.
# MUDE "sua_senha_secreta_aqui" para uma senha forte e única.
DB_PASSWORD=sua_senha_secreta_aqui

# Email e senha do administrador inicial do Wiki.js (opcional).
# Descomente e preencha para configurar o administrador automaticamente no primeiro boot.
# WIKI_ADMIN_EMAIL=admin@exemplo.com
# WIKI_ADMIN_PASSWORD=sua_senha_admin_aqui
```

**ATENÇÃO:** É crucial que você substitua `sua_senha_secreta_aqui` por uma senha forte e única.

### Passo 3.3: Criar o Arquivo Docker Compose (`docker-compose.yml`)

Este arquivo define os dois serviços necessários: o banco de dados **PostgreSQL** e a aplicação **Wiki.js**.

Crie o arquivo `docker-compose.yml` com a seguinte estrutura:

```yaml
version: '3.5'

services:
  database:
    image: postgres:16-alpine
    env_file:
      - .env
    container_name: wiki_db
    environment:
      POSTGRES_USER: wiki_user
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: wiki_db
    volumes:
      # Persiste os dados do banco de dados no diretório local ./data/db
      - ./data/db:/var/lib/postgresql/data
    restart: always

  wiki:
    image: ghcr.io/requarks/wiki:2
    env_file:
      - .env
    container_name: wiki_app
    environment:
      DB_TYPE: postgres
      DB_HOST: database
      DB_PORT: 5432
      DB_USER: wiki_user
      DB_PASS: ${DB_PASSWORD}
      DB_NAME: wiki_db
      # Configuração inicial do administrador (opcional)
      # WIKI_ADMIN_EMAIL: ${WIKI_ADMIN_EMAIL}
      # WIKI_ADMIN_PASSWORD: ${WIKI_ADMIN_PASSWORD}
    ports:
      # Mapeia a porta 80 do seu host para a porta 3000 do container Wiki.js
      - "80:3000"
    depends_on:
      - database
    volumes:
      # Persiste os arquivos de configuração e uploads do Wiki.js
      - ./data/wiki:/var/lib/wikijs
    restart: always
```

**Detalhes da Configuração:**

*   **`database`:** Utiliza a imagem oficial do PostgreSQL. O volume `./data/db` garante que seus dados sejam persistidos mesmo se o container for recriado.
*   **`wiki`:** Utiliza a imagem oficial do Wiki.js.
    *   A porta `80:3000` significa que você acessará o wiki pela porta 80 (padrão HTTP) do seu servidor. Se a porta 80 estiver em uso, você pode mudá-la para, por exemplo, `"8080:3000"`.
    *   O parâmetro `depends_on: database` garante que o container do banco de dados inicie antes do container do wiki.

## 4. Inicialização do Servidor Wiki

Com os arquivos configurados, o servidor wiki pode ser iniciado com um único comando:

```bash
docker compose up -d
```

Este comando fará o seguinte:
1.  Baixará as imagens Docker necessárias (PostgreSQL e Wiki.js).
2.  Criará e iniciará os containers `wiki_db` e `wiki_app`.
3.  Executará em segundo plano (`-d` de *detached*).

Aguarde alguns minutos para que o PostgreSQL inicie e o Wiki.js conclua a configuração inicial.

Para verificar o *status* dos containers, use:

```bash
docker compose ps
```

## 5. Acesso e Configuração Inicial

Após a inicialização bem-sucedida, o seu servidor wiki estará acessível.

### Passo 5.1: Acessar a Interface

Abra seu navegador e digite o endereço IP ou nome de domínio do seu servidor. Se estiver rodando localmente e usou a porta 80, acesse:

```
http://localhost
```

Se você alterou a porta para 8080, acesse: `http://localhost:8080`.

### Passo 5.2: Configuração do Administrador

Na primeira vez que você acessar, o Wiki.js solicitará que você crie a conta de administrador.

1.  Preencha o **Nome de Usuário**, **Email** e **Senha** para a sua conta de administrador.
2.  Clique em **Instalar** (ou equivalente).

Se você preencheu as variáveis `WIKI_ADMIN_EMAIL` e `WIKI_ADMIN_PASSWORD` no arquivo `.env` (Passo 3.2), esta etapa será ignorada e a conta de administrador será criada automaticamente.

## 6. Comandos Úteis

| Comando | Descrição |
| :--- | :--- |
| `docker compose up -d` | Inicia os containers em segundo plano. |
| `docker compose down` | Para e remove os containers, mas **mantém os volumes de dados** (seus dados wiki e DB). |
| `docker compose down -v` | Para e remove os containers e **todos os volumes de dados**. **Use com cautela!** |
| `docker compose logs -f wiki` | Exibe os logs em tempo real do container Wiki.js para *troubleshooting*. |
| `docker compose restart` | Reinicia todos os serviços definidos. |

---

## Referências

[1] Wiki.js - The most powerful and extensible open source wiki software: https://js.wiki/
[2] Docker Compose Documentation: https://docs.docker.com/compose/
