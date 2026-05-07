class FilmeService:

    def __init__(self, repository):
        self.repository = repository

    def cadastrar_filme(self, filme):

        if not filme.titulo:
            raise Exception("Título obrigatório.")

        if filme.duracao <= 0:
            raise Exception("Duração inválida.")

        self.repository.salvar(filme)