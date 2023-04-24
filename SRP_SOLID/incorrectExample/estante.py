class Estante:
    
    def __init__(self):
        self.livros = []
        
    def addLivro(self, livro):
        self.livros.append(livro) 
        
    def removeLivro(self, livro):
        self.livros.remove(livro)
        
    def listarLivros(self):
       for livro in self.livros:
           return livro