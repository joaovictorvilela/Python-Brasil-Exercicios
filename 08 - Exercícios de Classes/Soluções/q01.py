# Criando a classe bola
class Bola(object):
    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material

    def TrocarCor(self, NovaCor):
        self.__cor = NovaCor

    def MostrarCor(self):
        return self.__cor


# Testando a classe bola
"""
bola = Bola('Azul', 50, 'Plástico')
print(bola.MostrarCor())
bola.TrocarCor('Vermelho')
print(bola.MostrarCor())
"""