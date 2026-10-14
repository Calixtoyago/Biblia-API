from pydantic import BaseModel

class Versiculo(BaseModel):
    numero: int
    texto: str

class CapituloResponse(BaseModel):
    nome: str
    capitulo: int
    versiculos: list[Versiculo]

class VersiculoResponse(BaseModel):
    nome: str
    capitulo: int
    versiculo: int
    texto: str

class LivroResponse(BaseModel):
    abv: str
    nome: str
    testamento: str
    capitulos: int
    versiculos: int