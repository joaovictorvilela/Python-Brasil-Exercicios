class Macaco(object):
    def __init__(self, nome):
        self.nome = nome
        self.estomago = []
    
    def Comer(self, comida):
        self.estomago.append(comida)
        print(f'{self.nome} comeu {comida}')

    def VerEstomago(self):
        print(f'Estômago do {self.nome} - {self.estomago}')

    def Digerir(self):
        if (len(self.estomago) > 0):
            print(f'{self.nome} digeriu {self.estomago[-1]}')
            self.estomago.pop(-1)
