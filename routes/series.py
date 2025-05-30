from fastapi import APIRouter
from models.models import Serie
from utils.crud import executar_insert, executar_select

router = APIRouter(prefix="/serie")

@router.post("/")
def criar(obj: Serie):
    query = "INSERT INTO serie (id, titulo, descricao, ano_lancamento, id_categoria) VALUES (%s, %s, %s, %s, %s)"
    params = (obj.id, obj.titulo, obj.descricao, obj.ano_lancamento, obj.id_categoria)
    last_id = executar_insert(query, params)
    return {"id": last_id, "mensagem": "Serie criada com sucesso"}

@router.get("/")
def listar():
    return executar_select("SELECT * FROM serie")
