from app.backend.repositories.livros_repository import buscar_livro, buscar_todos_livros
from fastapi import HTTPException

def buscar_livro_service(livro_abv):
    livro = buscar_livro(livro_abv)
    if livro is None:
        raise HTTPException(404, "Livro não encontrado")
    return livro


def buscar_todos_livros_service():
    livros = buscar_todos_livros()
    if livros is None:
        raise HTTPException(404, "Nenhum livro encontrado")
    return livros