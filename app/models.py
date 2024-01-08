from pydantic import BaseModel

class Task(BaseModel):
    id: int
    titulo: str
    descricao: str = None
    concluida: bool