from fastapi import APIRouter
from models.models import Ator
from utils.crud import executar_insert, executar_select

router = APIRouter(prefix="/ator")

@router.post("/")
def criar(obj: Ator):
    query = "INSERT INTO ator (id, nome) VALUES (%s, %s)"
    params = (obj.id, obj.nome)
    last_id = executar_insert(query, params)
    return {"id": last_id, "mensagem": "Ator criado com sucesso"}

@router.get("/")
def listar():
    return executar_select("SELECT * FROM ator")
