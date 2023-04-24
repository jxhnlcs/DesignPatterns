from livros import Livros
from estante import Estante

livro = Livros("Mundo em caos", "Patrick Ness", "500", "2020")
estante = Estante()
estante.addLivro(livro)

print(estante.listarLivros())