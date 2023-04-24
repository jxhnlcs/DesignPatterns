from generator import Generator
from splitter import Splitter
from verifier import Verifier


class MagicSquareGenerator:
    def generate(self, size: int):
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier()

        while True:
            
            lista = []
            for x in range(size):
                lista.append(self.generator.generate(size))
                
            resultadoSplitter = self.splitter.split(lista)
            verificacao = self.verifier.verify(resultadoSplitter)
            
            if verificacao == False:
                pass
            else:
                break
        
        return lista