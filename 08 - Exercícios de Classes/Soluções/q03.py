class Retangulo(object):
    def __init__(self, LadoA, LadoB):
        self.__LadoA = LadoA
        self.__LadoB = LadoB

    def MudarValorDosLados(self, NovoLadoA, NovoLadoB):
        self.__LadoA = NovoLadoA
        self.__LadoB = NovoLadoB

    def RetornarValorDosLados(self):
        return f'Valor do lado A: {self.__LadoA}\nValor do lado B: {self.__LadoB}'

    def CalcularArea(self):
        return f'Área: {self.__LadoA * self.__LadoB:.2f}m²'

    def CalcularPerimentro(self):
        return f'Perímetro: {2 * self.__LadoA + 2 * self.__LadoB:.2f}cm'
        
"""
Rentagulo = Retangulo(5,10)
print(Rentagulo.CalcularArea())
Rentagulo.MudarValorDosLados(3,10)
print(Rentagulo.CalcularArea())
print(Rentagulo.CalcularPerimentro())
"""
