from fastapi import APIRouter
from models.models import Ator_Serie
from utils.crud import executar_insert, executar_select

router = APIRouter(prefix="/ator_serie")

@router.post("/")
def criar(obj: Ator_Serie):
    query = "INSERT INTO ator_serie (id_ator, id_serie, personagem) VALUES (%s, %s, %s)"
    params = (obj.id_ator, obj.id_serie, obj.personagem)
    last_id = executar_insert(query, params)
    return {"id": last_id, "mensagem": "Ator_Serie criado com sucesso"}

@router.get("/")
def listar():
    return executar_select("SELECT * FROM ator_serie")