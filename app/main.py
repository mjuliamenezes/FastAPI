from fastapi import FastAPI, HTTPException
from app.models import Task
from app.routes import tasks, consultar_cnpj

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
    
app.include_router(tasks.router)
app.include_router(consultar_cnpj.router)