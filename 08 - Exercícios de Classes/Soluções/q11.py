class Carro(object):
    def __init__(self, consumo, tanque = 0):
        self.consumo = consumo
        self.tanque = tanque

    def AdicionarGasolina(self, valor):
        self.tanque += valor

    def ObterGasolina(self):
        return f'Nível de gasolina: {self.tanque:.2f}l'

    def Andar(self, distancia):
        gasto = distancia / self.consumo
        self.tanque -= gasto