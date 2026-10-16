from fastapi import FastAPI
from app.routers.livros_routers import router as livros_router
from app.routers.versiculos_routers import router as versiculos_router

app = FastAPI(title="Bíblia API", version="0.3.1")

app.include_router(livros_router)
app.include_router(versiculos_router)

@app.get("/")
def home():
    return {
        "message": "Biblia API",
        "versão": "0.3.1",
        "créditos": "Todas as Escrituras em português citadas são da Bíblia Livre (BLIVRE), Copyright © Diego Santos, Mario Sérgio, e Marco Teles, http://sites.google.com/site/biblialivre/ - outubro de 2017. Licença Creative Commons Atribuição 3.0 Brasil (http://creativecommons.org/licenses/by/3.0/br/). Reprodução permitida desde que devidamente mencionados fonte e autores."
        }