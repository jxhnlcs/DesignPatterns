from livros import Livros
from estante import Estante
from pesquisa import Pesquisa


estante = Estante()
estante.addLivro(Livros("Mundo em caos", "Patrick Ness", "500", "2020"))
estante.addLivro(Livros("O ultimo Adeus", "Cynthia hand", "352", "2016"))
estante.addLivro(Livros("A biblioteca da meia noite", "Matt Haig", "308", "2021"))

Pesquisa = Pesquisa(estante)
livrosEncontrados = Pesquisa.pesquisar_titulo("A biblioteca da meia noite")
print(livrosEncontrados)

