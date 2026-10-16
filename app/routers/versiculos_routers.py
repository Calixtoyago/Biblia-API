from fastapi import APIRouter
from app.schemas import VersiculoResponse, CapituloResponse
from app.services.versiculos_services import buscar_versiculo_service, buscar_capitulo_service, buscar_intervalo_service, vesiculo_aleatorio_service

router = APIRouter(prefix="/biblia", tags=["biblia"])

#GET - listar versiculo
@router.get("/{livro_abv}/{capitulo}/{versiculo}", response_model=VersiculoResponse)
def buscar_versiculo_router(livro_abv: str, capitulo: int, versiculo: int):
    return buscar_versiculo_service(livro_abv, capitulo, versiculo)

#GET - listar versiculo aleatorio
@router.get("/random", response_model=VersiculoResponse)
def vesiculo_aleatorio_router():
    return vesiculo_aleatorio_service()

#GET - listar versiculos de um capitulo
@router.get("/{livro_abv}/{capitulo}", response_model=CapituloResponse)
def buscar_capitulo_router(livro_abv: str, capitulo: int):
    return buscar_capitulo_service(livro_abv, capitulo)

#GET - listar versiculos de um intervalo de um capitulo
@router.get("/{livro_abv}/{capitulo}/{inicio}/{fim}", response_model=CapituloResponse)
def buscar_intervalo_router(livro_abv: str, capitulo: int, inicio: int, fim: int):
    return buscar_intervalo_service(livro_abv, capitulo, inicio, fim)
