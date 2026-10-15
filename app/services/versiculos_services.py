from app.repositories.versiculos_repository import buscar_versiculo_repository, buscar_capitulo_repository
from fastapi import HTTPException

def buscar_versiculo_service(livro_abv, capitulo, versiculo):
    verso = buscar_versiculo_repository(livro_abv, capitulo, versiculo)
    if verso is None:
        raise HTTPException(404, "Livro não encontrado")
    return verso

def buscar_capitulo_service(livro_abv, capitulo):
    capitulo_versos = buscar_capitulo_repository(livro_abv, capitulo)
    if capitulo_versos is None:
        raise HTTPException(404, "Capítulo não encontrado")
    return capitulo_versos