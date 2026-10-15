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

def buscar_capitulo_repository(livro_abv, capitulo):
    livro_query = "SELECT id, nome FROM livros WHERE lower(abv) = lower(?)"
    versiculos_query = """
        SELECT versiculo AS numero, texto
        FROM biblia
        WHERE livro_id = ? AND capitulo = ?
        ORDER BY versiculo
    """
    with get_con() as con:
        livro = con.execute(livro_query, (livro_abv,)).fetchone()
        if livro is None:
            return None
        versiculos = con.execute(versiculos_query, (livro["id"], capitulo)).fetchall()

    if not versiculos:
        return None
    
    return {
        "nome": livro["nome"],
        "capitulo": capitulo,
        "versiculos": [dict(verso) for verso in versiculos]
    }