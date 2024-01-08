# Projeto FastAPI de Gerenciamento de Tarefas

Este projeto consiste em uma API utilizando FastAPI para gerenciar uma lista de tarefas. A API permite operações CRUD (Criar, Ler, Atualizar, Deletar) para manipulação das tarefas. Além disso, foi implementada uma rota de consulta de CNPJ utilizando a API do CNPJ.WS. Testes simples foram desenvolvidos com o pytest para garantir o correto funcionamento dos endpoints.

## Instruções para Configuração e Execução (Windows)

1. **Criar Ambiente Virtual:**
   python -m venv venv

2. **Ativar Ambiente Virtual:**
    venv\Scripts\activate

3. **Instalar Dependências:**
    pip install -r requirements.txt

4. **Rodar o Servidor:**
    uvicorn app.main:app --reload

5. **Explorar a documentação interativa da API:**
    Acesse http://127.0.0.1:8000/docs


## Instruções para Execução dos Testes

1. **Ativar Ambiente Virtual (em outro terminal):**
    venv\Scripts\activate

2. **Executar os Testes:**
    pytest

3. **Verificar Resultados:**
    No console, verifique os resultados dos testes para garantir que todos passaram.