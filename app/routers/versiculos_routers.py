from fastapi import APIRouter
from app.schemas import VersiculoResponse
from app.services.versiculos_services import buscar_versiculo_service

router = APIRouter(prefix="/biblia", tags=["biblia"])

#GET - listar versiculo
@router.get("/{livro_abv}/{capitulo}/{versiculo}", response_model=VersiculoResponse)
def buscar_versiculo_router(livro_abv: str, capitulo: int, versiculo: int):
    return buscar_versiculo_service(livro_abv, capitulo, versiculo)
