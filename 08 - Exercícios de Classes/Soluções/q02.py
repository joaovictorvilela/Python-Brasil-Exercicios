# Defininado a classe Quadrado

class Quadrado(object):
    def __init__(self, TamanhoDoLado):
        self.__TamanhoDoLado = TamanhoDoLado

    def MostrarValorDoLado(self):
        return self.__TamanhoDoLado

    def TrocarValorDoLado(self, NovoTamanho):
        self.__TamanhoDoLado = NovoTamanho

    def CalcularArea(self):
        return self.__TamanhoDoLado * self.__TamanhoDoLado

# testando a classe

"""
Quadrado = Quadrado(8)
print(Quadrado.MostrarValorDoLado())
Quadrado.TrocarValorDoLado(25)
print(Quadrado.MostrarValorDoLado())
print(Quadrado.CalcularArea())
"""
