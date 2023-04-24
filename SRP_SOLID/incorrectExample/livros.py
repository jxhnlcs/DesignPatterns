class Livros:
    def __init__(self, titulo, autor, paginas, ano):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.ano = ano
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"