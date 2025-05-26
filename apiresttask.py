from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tarefa(BaseModel):
    id: int
    titulo: str
    concluida: bool = False

tarefas: List[Tarefa] = []

@app.get("/", tags=["Raiz"])
def raiz():
    return {"mensagem": "API de Tarefas com FastAPI"}

@app.get("/tarefas", response_model=List[Tarefa], tags=["Tarefas"])
def listar_tarefas():
    return tarefas

@app.post("/tarefas", response_model=Tarefa, status_code=201, tags=["Tarefas"])
def criar_tarefa(tarefa: Tarefa):
    tarefas.append(tarefa)
    return tarefa

@app.get("/tarefas/{tarefa_id}", response_model=Tarefa, tags=["Tarefas"])
def obter_tarefa(tarefa_id: int):
    for tarefa in tarefas:
        if tarefa.id == tarefa_id:
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.put("/tarefas/{tarefa_id}", response_model=Tarefa, tags=["Tarefas"])
def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: Tarefa):
    for i, tarefa in enumerate(tarefas):
        if tarefa.id == tarefa_id:
            tarefas[i] = tarefa_atualizada
            return tarefa_atualizada
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.delete("/tarefas/{tarefa_id}", status_code=204, tags=["Tarefas"])
def deletar_tarefa(tarefa_id: int):
    for i, tarefa in enumerate(tarefas):
        if tarefa.id == tarefa_id:
            tarefas.pop(i)
            return
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
