# Defininado a classe Quadrado

class Quadrado(object):
    def __init__(self, TamanhoDoLado):
        self.TamanhoDoLado = TamanhoDoLado

    def MostrarValorDoLado(self):
        return self.TamanhoDoLado

    def TrocarValorDoLado(self, NovoTamanho):
        self.TamanhoDoLado = NovoTamanho

    def CalcularArea(self):
        return self.TamanhoDoLado * self.TamanhoDoLado

# testando a classe

"""
Quadrado = Quadrado(8)
print(Quadrado.MostrarValorDoLado())
Quadrado.TrocarValorDoLado(25)
print(Quadrado.MostrarValorDoLado())
print(Quadrado.CalcularArea())
"""
