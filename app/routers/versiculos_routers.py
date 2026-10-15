from fastapi import APIRouter
from app.schemas import VersiculoResponse, CapituloResponse
from app.services.versiculos_services import buscar_versiculo_service, buscar_capitulo_service

router = APIRouter(prefix="/biblia", tags=["biblia"])

#GET - listar versiculo
@router.get("/{livro_abv}/{capitulo}/{versiculo}", response_model=VersiculoResponse)
def buscar_versiculo_router(livro_abv: str, capitulo: int, versiculo: int):
    return buscar_versiculo_service(livro_abv, capitulo, versiculo)

#GET - listar versiculos de um capitulo
@router.get("/{livro_abv}/{capitulo}", response_model=CapituloResponse)
def buscar_capitulo_router(livro_abv: str, capitulo: int):
    return buscar_capitulo_service(livro_abv, capitulo)
