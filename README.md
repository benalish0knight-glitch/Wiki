# 🌟 Guia de Utilização Rápida: Seu Wiki Gollum

Bem-vindo(a) ao nosso Wiki, alimentado pelo **Gollum**!

Este Wiki é um repositório de conhecimento colaborativo onde você pode facilmente **visualizar, adicionar e atualizar** informações usando a interface do Gollum e o poder do controle de versão do **Git**.

---

## 🧐 O Que é o Gollum?

O Gollum é um aplicativo de wiki simples baseado no Git. Isso significa que **todas as páginas e todo o histórico de alterações são armazenados como um repositório Git**. Isso nos permite ter:
* **Controle de Versão:** Rastreamento completo de quem mudou o quê e quando.
* **Colaboração:** Fluxo de trabalho robusto e familiar para quem usa Git.

---

## 🚀 Como Contribuir (Adicionar/Atualizar Conteúdo)

A principal força deste Wiki reside na sua capacidade de ser atualizado via Git. Você tem **duas** formas principais de interagir com o conteúdo:

### Opção 1: Usando a Interface Web (Para Edições Rápidas)

Para a maioria das edições, o próprio Gollum facilita a vida.

1.  **Acesse a Página:** Navegue até a página que deseja editar ou crie uma nova.
2.  **Clique em "Editar":** Na parte superior, clique no botão **"Editar"**.
3.  **Faça as Alterações:** Edite o conteúdo. O Gollum suporta vários formatos de marcação (Markdown é o padrão e o mais recomendado).
4.  **Descreva a Mudança:** No campo **"Mensagem de Commit"**, **descreva de forma concisa** o que você alterou (Exemplo: "Adiciona seção sobre autenticação de API").
5.  **Salve:** Clique em **"Salvar"**.

> 💡 **Nota:** Ao salvar, o Gollum faz automaticamente um *commit* no repositório Git subjacente!

### Opção 2: Usando o Git Localmente (Para Mudanças Maiores ou Estruturais)

Para grandes mudanças, adição de vários arquivos, ou edição fora do navegador, use o fluxo de trabalho Git padrão.

#### 1. Clonar o Repositório

```bash
# Substitua <URL_DO_REPOSITORIO> pela URL real do nosso repositório Wiki
git clone <URL_DO_REPOSITORIO>
cd <nome-do-diretorio-wiki> 
2. Criar e Editar Páginas
Crie novos arquivos (as páginas do Wiki) ou edite os existentes em seu editor de código favorito.

Lembre-se: A extensão do arquivo define a sintaxe (ex: .md para Markdown, .rst para reStructuredText).

3. Fazer o Commit e o Push
Após fazer suas alterações, use os comandos padrão do Git:

Bash

# Adiciona todos os arquivos alterados (ou use o nome do arquivo específico)
git add . 

# Cria um commit com uma mensagem descritiva (Obrigatório!)
git commit -m "feat: Adiciona documentação inicial para o módulo de Pagamentos" 

# Envia as alterações para o repositório remoto (atualiza o Wiki)
git push origin master 
# (ou a branch principal que estiver sendo usada)
📚 Sintaxe de Conteúdo Recomendada
Recomendamos fortemente o uso da sintaxe Markdown (arquivos com extensão .md ou .markdown) por sua simplicidade e legibilidade.

Exemplo Rápido de Markdown:
Markdown

# Título Principal

## Subtítulo

Aqui está um parágrafo de texto normal.

* Item de lista 1
* Item de lista 2

**Texto em Negrito** e *Texto em Itálico*.

[Link de Exemplo](http://exemplo.com)
❓ Precisa de Ajuda?
Se tiver dúvidas sobre o processo de contribuição, entre em contato com [Mencione o canal/contato de suporte aqui, ex: o canal #wiki-suporte no Slack].

Feliz colaboração!

## 6. Comandos Úteis para subir gerir o container

| Comando | Descrição |
| :--- | :--- |
| `docker compose up -d` | Inicia os containers em segundo plano. |
| `docker compose down` | Para e remove os containers, mas **mantém os volumes de dados** (seus dados wiki e DB). |
| `docker compose down -v` | Para e remove os containers e **todos os volumes de dados**. **Use com cautela!** |
| `docker compose logs -f wiki` | Exibe os logs em tempo real do container Wiki.js para *troubleshooting*. |
| `docker compose restart` | Reinicia todos os serviços definidos. |

---

## Referências


https://github.com/gollum/gollum