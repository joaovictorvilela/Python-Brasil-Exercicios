class Retangulo(object):
    def __init__(self, LadoA, LadoB):
        self.LadoA = LadoA
        self.LadoB = LadoB

    def MudarValorDosLados(self, NovoLadoA, NovoLadoB):
        self.LadoA = NovoLadoA
        self.LadoB = NovoLadoB

    def RetornarValorDosLados(self):
        return f'Valor do lado A: {self.LadoA}\nValor do lado B: {self.LadoB}'

    def CalcularArea(self):
        return f'Área: {self.LadoA * self.LadoB:.2f}m²'

    def CalcularPerimentro(self):
        return f'Perímetro: {2 * self.LadoA + 2 * self.LadoB:.2f}cm'
        
"""
Rentagulo = Retangulo(5,10)
print(Rentagulo.CalcularArea())
Rentagulo.MudarValorDosLados(3,10)
print(Rentagulo.CalcularArea())
print(Rentagulo.CalcularPerimentro())
"""
