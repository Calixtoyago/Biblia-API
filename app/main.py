from fastapi import FastAPI
from app.routers.livros_routers import router as livros_router
from app.routers.versiculos_routers import router as versiculos_router

app = FastAPI(title="Bíblia API")

app.include_router(livros_router)
app.include_router(versiculos_router)

@app.get("/")
def home():
    return {"message": "Biblia API"}