import pytest
import requests

# Criando a URL base
url_base = "http://127.0.0.1:8000"

# Criando uma Task de Base para os Teste (mock)
task_base = {"id": 1, "titulo": "Titulo Teste 1", "descricao": "Descrição Teste 1", "concluida": False}

# Adicionar tarefa 
# Teste de sucesso
def test_add_task_success():
    response = requests.post(f"{url_base}/tarefas?titulo={task_base['titulo']}&descricao={task_base['descricao']}", json=task_base)
    assert response.status_code == 200
    assert response.json()["titulo"] == "Titulo Teste 1"
    assert response.json()["descricao"] == "Descrição Teste 1"


# Listar todas as tarefas
# Teste de sucesso
def test_get_tasks_success():
    response = requests.get(f"{url_base}/tarefas")
    assert response.status_code == 200
    assert "tarefas" in response.json()


# Listar tarefa com ID específico
# Teste de sucesso
def test_get_task_success(): 
    # teste de integração
    response_add_task = requests.post(f"{url_base}/tarefas?titulo={task_base['titulo']}&descricao={task_base['descricao']}", json=task_base)
    task_id = response_add_task.json()["id"]

    response_get_task = requests.get(f"{url_base}/tarefas/{task_id}")
    assert response_get_task.status_code == 200
    assert response_get_task.json()["id"] == task_id

# Teste de erro: acessando tarefa inexistente
def test_get_task_not_found():
    response = requests.get(f"{url_base}/tarefas/999999")  # Um ID que não existe
    assert response.status_code == 404
    assert "detail" in response.json()
    assert response.json()["detail"] == "Tarefa não encontrada"


# Atualizar tarefa
# Teste de sucesso
def test_update_task_success():
    # teste de integração
    response_add_task = requests.post(f"{url_base}/tarefas?titulo={task_base['titulo']}&descricao={task_base['descricao']}", json=task_base)
    task_id = response_add_task.json()["id"]

    update_data = {"id": 0, "titulo": "Novo Título", "descricao": "Nova Descrição", "concluida": True}
    response_update_task = requests.put(f"{url_base}/tarefas/{task_id}", json=update_data)

    assert response_update_task.status_code == 200
    assert response_update_task.json()["status"] == "Tarefa atualizada"

# Teste de erro
def test_update_task_not_found():
    update_data = {"id": 0, "titulo": "Novo Título", "descricao": "Nova Descrição", "concluida": True}
    response = requests.put(f"{url_base}/tarefas/999999", json=update_data)  # Um ID que não existe
    assert response.status_code == 404
    assert "detail" in response.json()
    assert response.json()["detail"] == "Tarefa não encontrada"


# Deletar tarefa
# Teste de sucesso
def test_delete_task_success():
    # teste de integração
    response_add_task = requests.post(f"{url_base}/tarefas?titulo={task_base['titulo']}&descricao={task_base['descricao']}", json=task_base)
    task_id = response_add_task.json()["id"]

    response_delete_task = requests.delete(f"{url_base}/tarefas/{task_id}")
    assert response_delete_task.status_code == 200
    assert response_delete_task.json()["status"] == "Tarefa deletada"

# Teste de erro: tarefa inexistente
def test_delete_task_not_found():
    response = requests.delete(f"{url_base}/tarefas/999999")  # Um ID que não existe
    assert response.status_code == 404
    assert "detail" in response.json()
    assert response.json()["detail"] == "Tarefa não encontrada"