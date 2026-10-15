import sqlite3

con = sqlite3.connect("biblia.db")
db = con.cursor()

livros_dict = {
    "GEN": ["Gn", "Gênesis"],
    "EXO": ["Ex", "Êxodo"],
    "LEV": ["Lv", "Levíticos"],
    "NUM": ["Nm", "Números"],
    "DEU": ["Dt", "Deuteronômios"],
    "JOS": ["Js", "Josué"],
    "JDG": ["Jz", "Juízes"],
    "RUT": ["Rt", "Rute"],
    "1SA": ["1Sm", "1 Samuel"],
    "2SA": ["2Sm", "2 Samuel"],
    "1KI": ["1Rs", "1 Reis"],
    "2KI": ["2Rs", "2 Reis"],
    "1CH": ["1Cr", "1 Crônicas"],
    "2CH": ["2Cr", "2 Crônicas"],
    "EZR": ["Ed", "Esdras"],
    "NEH": ["Ne", "Neemias"],
    "EST": ["Et", "Ester"],
    "JOB": ["Jó", "Jó"],
    "PSA": ["Sl", "Salmos"],
    "PRO": ["Pv", "Provérbios"],
    "ECC": ["Ec", "Eclesiastes"],
    "SOL": ["Ct", "Cantares"],
    "ISA": ["Is", "Isaías"],
    "JER": ["Jr", "Jeremias"],
    "LAM": ["Lm", "Lamentações"],
    "EZE": ["Ez", "Ezequiel"],
    "DAN": ["Dn", "Daniel"],
    "HOS": ["Os", "Oséias"],
    "JOE": ["Jl", "Joel"],
    "AMO": ["Am", "Amós"],
    "OBA": ["Ob", "Obadias"],
    "JON": ["Jn", "Jonas"],
    "MIC": ["Mq", "Miqueias"],
    "NAH": ["Na", "Naum"],
    "HAB": ["Hc", "Habacuque"],
    "ZEP": ["Sf", "Sofonias"],
    "HAG": ["Ag", "Ageu"],
    "ZEC": ["Zc", "Zacarias"],
    "MAL": ["Ml", "Malaquias"],
    "MAT": ["Mt", "Mateus"],
    "MAR": ["Mc", "Marcos"],
    "LUK": ["Lc", "Lucas"],
    "JOH": ["Jo", "João"],
    "ACT": ["At", "Atos"],
    "ROM": ["Rm", "Romanos"],
    "1CO": ["1Co", "1 Coríntios"],
    "2CO": ["2Co", "2 Coríntios"],
    "GAL": ["Gl", "Gálatas"],
    "EPH": ["Ef", "Efésios"],
    "PHI": ["Fp", "Filipenses"],
    "COL": ["Cl", "Colossenses"],
    "1TH": ["1Ts", "1 Tessalonicenses"],
    "2TH": ["2Ts", "2 Tessalonicenses"],
    "1TI": ["1Tm", "1 Timóteo"],
    "2TI": ["2Tm", "2 Timóteo"],
    "TIT": ["Tt", "Tito"],
    "PHM": ["Fm", "Filemon"],
    "HEB": ["Hb", "Hebreus"],
    "JAM": ["Tg", "Tiago"],
    "1PE": ["1Pe", "1 Pedro"],
    "2PE": ["2Pe", "2 Pedro"],
    "1JO": ["1Jo", "1 João"],
    "2JO": ["2Jo", "2 João"],
    "3JO": ["3Jo", "3 João"],
    "JUD": ["Jd", "Judas"],
    "REV": ["Ap", "Apocalipse"]
}

def criar_banco():
    db.executescript("""
        DROP TABLE IF EXISTS livros;
        DROP TABLE IF EXISTS biblia;
        DROP TABLE IF EXISTS biblia_fts;

        CREATE TABLE IF NOT EXISTS livros (
            id INTEGEr PRIMARY KEY,
            abv TEXT NOT NULL UNIQUE,
            nome TEXT NOT NULL UNIQUE,
            testamento TEXT NOT NULL CHECK(testamento IN ('AT', 'NT')),
            capitulos INTEGER NOT NULL,
            versiculos INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS biblia (
            livro_id TEXT NOT NULL REFERENCES livros(id),
            capitulo INTEGER NOT NULl CHECK(capitulo > 0),
            versiculo INTEGER NOT NULL CHECK(versiculo > 0),
            texto TEXT NOT NULL,
            PRIMARY KEY(livro_id, capitulo, versiculo)
        );

        CREATE VIRTUAL TABLE IF NOT EXISTS biblia_fts USING fts5(
            texto,
            content='biblia',
            content_rowid='rowid',
            tokenize='unicode61 remove_diacritics 2'
        );
    """)

def inserir_livros():
    contagem = {}
    with open("docs/bliv-tr_vpl.txt", "r", encoding="utf-8-sig") as biblia:
        for linha in biblia:
            codigo, ref, _texto = linha.split(" ", 2)   # "GEN", "1:1", "No princípio..."
            capitulo = int(ref.split(":")[0])

            c = contagem.setdefault(codigo, [0, 0])
            c[0] = max(c[0], capitulo)
            c[1] += 1

    testamento = "AT"
    for codigo, (abv, nome) in livros_dict.items():
        if abv == "Mt":
            testamento = "NT"
        capitulos, versiculos = contagem[codigo]

        db.execute("""
            INSERT INTO livros (abv, nome, testamento, capitulos, versiculos)
            VALUES (?, ?, ?, ?, ?)
        """, (abv, nome, testamento, capitulos, versiculos))

def inserir_versiculos():
    with open("docs/bliv-tr_vpl.txt", "r", encoding="utf-8-sig") as biblia:
        for linha in biblia:
            codigo, ref, texto = linha.split(" ", 2)

            capitulo = ref.split(":")[0]
            versiculo = ref.split(":")[1]

            abv = livros_dict[codigo][0]
            livro_id = db.execute("SELECT id FROM livros WHERE abv=:abv", {"abv": abv}).fetchone()[0]

            texto = texto.strip()

            db.execute("""
                INSERT INTO biblia (livro_id, capitulo, versiculo, texto)
                VALUES (?, ?, ?, ?)
            """, (livro_id, capitulo, versiculo, texto))

criar_banco()
inserir_livros()
inserir_versiculos()
con.commit()
con.close()