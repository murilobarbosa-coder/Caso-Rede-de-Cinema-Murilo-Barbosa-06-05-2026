from model.filme import Filme
from repository.filme_repository import FilmeRepository
from service.filme_service import FilmeService
from controller.filme_controller import FilmeController


repository = FilmeRepository("filmes.json")
service = FilmeService(repository)
controller = FilmeController(service)

filme = Filme(
    "Interestelar",
    169,
    "12 anos",
    "Ficção Científica",
    "Christopher Nolan"
)

controller.cadastrar(filme)