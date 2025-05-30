from fastapi import APIRouter
from models.models import Categoria
from utils.crud import executar_insert, executar_select

router = APIRouter(prefix="/categoria")

@router.post("/")
def criar(obj: Categoria):
    query = "INSERT INTO categoria (id, nome) VALUES (%s, %s)"
    params = (obj.id, obj.nome)
    last_id = executar_insert(query, params)
    return {"id": last_id, "mensagem": "Categoria criada com sucesso"}

@router.get("/")
def listar():
    return executar_select("SELECT * FROM categoria")
