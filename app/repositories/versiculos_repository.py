from app.db import get_con

def buscar_versiculo_repository(livro_abv, capitulo, versiculo):
    # livro_id = con.execute("SELECT id FROM livros WHERE abv = ?", (livro_abv, )).fetchone()

    query = """
        SELECT l.nome, b.capitulo, b.versiculo, b.texto
        FROM biblia b
        JOIN livros l ON b.livro_id = l.id
        WHERE l.abv = ? AND b.capitulo = ? AND b.versiculo = ?
    """
    with get_con() as con:
        resultado = con.execute(query, (livro_abv, capitulo, versiculo,)).fetchone()
    return dict(resultado) if resultado else None