class Pesquisa: 
    def __init__(self, estante):
        self.estante = estante

    def pesquisar_titulo(self, titulo):
        for livro in self.estante.livros:
            if livro.titulo == titulo:
                return livro