from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from app.routers.livros_routers import router as livros_router
from app.routers.versiculos_routers import router as versiculos_router

VERSAO = "0.6.0"

app = FastAPI(title="Bíblia API", version=VERSAO)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(livros_router)
app.include_router(versiculos_router)

FRONTEND_DIR = Path(__file__).resolve().parent / "frontend"
app.mount("/web", StaticFiles(directory=FRONTEND_DIR, html=True), name="web")

@app.get("/", include_in_schema=False)
def raiz():
    return RedirectResponse(url="/web/")

@app.get("/info")
def info():
    return {
        "message": "Biblia API",
        "versão": VERSAO,
        "créditos": "Todas as Escrituras em português citadas são da Bíblia Livre (BLIVRE), Copyright © Diego Santos, Mario Sérgio, e Marco Teles, http://sites.google.com/site/biblialivre/ - outubro de 2017. Licença Creative Commons Atribuição 3.0 Brasil (http://creativecommons.org/licenses/by/3.0/br/). Reprodução permitida desde que devidamente mencionados fonte e autores."
    }
