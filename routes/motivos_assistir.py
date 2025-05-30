from fastapi import APIRouter
from models.models import Motivo_Assistir
from utils.crud import executar_insert, executar_select

router = APIRouter(prefix="/motivo_assistir")

@router.post("/")
def criar(obj: Motivo_Assistir):
    query = "INSERT INTO motivo_assistir (id, id_serie, motivo) VALUES (%s, %s, %s)"
    params = (obj.id, obj.id_serie, obj.motivo)
    last_id = executar_insert(query, params)
    return {"id": last_id, "mensagem": "Motivo_Assistir criado com sucesso"}

@router.get("/")
def listar():
    return executar_select("SELECT * FROM motivo_assistir")
        