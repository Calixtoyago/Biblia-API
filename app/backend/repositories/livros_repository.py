from app.backend.db import get_con

def buscar_livro(livro_abv):
    query = "SELECT abv, nome, testamento, capitulos, versiculos FROM livros WHERE lower(abv) = lower(?) "
    with get_con() as con:
        resultado = con.execute(query, (livro_abv,)).fetchone()
    return dict(resultado) if resultado else None

def buscar_todos_livros():
    query = "SELECT abv, nome, testamento, capitulos, versiculos FROM livros"
    with get_con() as con:
        resultado = con.execute(query).fetchall()
    return [dict(livro) for livro in resultado]