import json
import os


class FilmeRepository:

    def __init__(self, arquivo):
        self.arquivo = arquivo

    def salvar(self, filme):

        filmes = []

        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as f:
                try:
                    filmes = json.load(f)
                except json.JSONDecodeError:
                    filmes = []

        filmes.append(filme.to_dict())

        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(filmes, f, indent=4, ensure_ascii=False)

        print("Filme salvo com sucesso.")