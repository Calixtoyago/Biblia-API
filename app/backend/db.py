import sqlite3
from contextlib import contextmanager
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent.parent / "biblia.db"   # biblia-api/biblia.db

@contextmanager
def get_con():
    con = sqlite3.connect(DB_PATH.as_uri() + "?mode=ro", uri=True)  # somente leitura
    con.row_factory = sqlite3.Row
    try:
        yield con
    finally:
        con.close()