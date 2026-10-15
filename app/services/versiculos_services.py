from app.repositories.versiculos_repository import buscar_versiculo_repository
from fastapi import HTTPException

def buscar_versiculo_service(livro_abv, capitulo, versiculo):
    verso = buscar_versiculo_repository(livro_abv, capitulo, versiculo)
    if verso is None:
        raise HTTPException(404, "Livro não encontrado")
    return verso