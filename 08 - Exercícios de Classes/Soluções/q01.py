# Criando a classe bola
class Bola(object):
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def TrocarCor(self, NovaCor):
        self.cor = NovaCor

    def MostrarCor(self):
        return self.cor


# Testando a classe bola
"""
bola = Bola('Azul', 50, 'Plástico')
print(bola.MostrarCor())
bola.TrocarCor('Vermelho')
print(bola.MostrarCor())
"""