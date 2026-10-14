from fastapi import APIRouter
from app.schemas import LivroResponse
from app.services.livros_services import buscar_livro_service, buscar_todos_livros_service

router = APIRouter(prefix="/livros", tags=["livros"])

#GET - listar usuarios
@router.get("/{livro_abv}", response_model=LivroResponse)
def buscar_livro_router(livro_abv: str):
    return buscar_livro_service(livro_abv)

@router.get("/", response_model=list[LivroResponse])
def buscar_todos_livros_router():
    return buscar_todos_livros_service()