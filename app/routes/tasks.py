from fastapi import APIRouter, HTTPException, Depends
from app.models import Task
from typing import Union

router = APIRouter()


# Lista de tarefas
tasks = []
task_id_counter = 1  # Para gerar IDs automaticamente


# Rota para adicionar uma nova tarefa
@router.post("/tarefas")
def add_task(titulo: str, descricao: str = None):
    global task_id_counter
    task = Task(id=task_id_counter, titulo=titulo, descricao=descricao, concluida=False)
    tasks.append(task)
    task_id_counter += 1
    return task

# Rota para obter todas as tarefas
@router.get("/tarefas")
def get_tasks():
    return {"tarefas": tasks}

# Rota para obter uma tarefa específica pelo ID
@router.get("/tarefas/{tarefa_id}")
def get_task(tarefa_id: int):
    for task in tasks:
        if task.id == tarefa_id:
            return task
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

# Rota para atualizar uma tarefa existente
@router.put("/tarefas/{tarefa_id}")
def update_task(tarefa_id: int, updated_task: Task):
    task_index = find_task_index(tarefa_id)

    if task_index is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    current_task = tasks[task_index]
    current_task.titulo = updated_task.titulo
    current_task.descricao = updated_task.descricao
    current_task.concluida = updated_task.concluida

    return {"status": "Tarefa atualizada"}

def find_task_index(tarefa_id: int) -> Union[int, None]:
    for index, task in enumerate(tasks):
        if task.id == tarefa_id:
            return index
    return None

# Rota para deletar uma tarefa pelo ID
@router.delete("/tarefas/{tarefa_id}")
def delete_task(tarefa_id: int):
    task_index = find_task_index(tarefa_id)

    if task_index is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    tasks.pop(task_index)
    return {"status": "Tarefa deletada"}