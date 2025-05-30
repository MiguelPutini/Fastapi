from fastapi import APIRouter
from models.models import Avaliacao_Serie
from utils.crud import executar_insert, executar_select

router = APIRouter(prefix="/avaliacao_serie")

@router.post("/")
def criar(obj: Avaliacao_Serie):
    query = "INSERT INTO avaliacao_serie (id, id_serie, nota, comentario, data_avaliacao) VALUES (%s, %s, %s, %s, %s)"
    params = (obj.id, obj.id_serie, obj.nota, obj.comentario, obj.data_avaliacao)
    last_id = executar_insert(query, params)
    return {"id": last_id, "mensagem": "Avaliacao_Serie criada com sucesso"}

@router.get("/")
def listar():
    return executar_select("SELECT * FROM avaliacao_serie")
