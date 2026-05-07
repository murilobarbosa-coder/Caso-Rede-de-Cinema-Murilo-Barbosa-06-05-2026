import sqlite3


conexao = sqlite3.connect("cinema.db")

cursor = conexao.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS filme (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        duracao INTEGER NOT NULL,
        classificacao_indicativa TEXT,
        genero TEXT,
        diretor TEXT
    )
    """
)

conexao.commit()

print("Tabela criada com sucesso.")