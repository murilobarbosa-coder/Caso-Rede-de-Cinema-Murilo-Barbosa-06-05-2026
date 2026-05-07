class Filme:

    def __init__(self, titulo, duracao,
                 classificacao_indicativa,
                 genero,
                 diretor):

        self.titulo = titulo
        self.duracao = duracao
        self.classificacao_indicativa = classificacao_indicativa
        self.genero = genero
        self.diretor = diretor

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "duracao": self.duracao,
            "classificacao_indicativa": self.classificacao_indicativa,
            "genero": self.genero,
            "diretor": self.diretor
        }