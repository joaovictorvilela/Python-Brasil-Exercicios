class Pessoa(object):
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def Envelhercer(self, anos):
        if (self.__idade < 21):
            self.__altura += 0.5
        self.__idade += anos

    def Engordar(self, peso):
        self.__peso += peso

    def Emagrecer(self, peso):
        if (peso <= self.__peso):
            self.__peso -= peso
    
    def Crescer(self, altura):
        self.__altura += altura

    def Mostrar(self):
        return f'Altura: {self.__altura}\nNome: {self.__nome}\nIdade: {self.__idade}\nPeso: {self.__peso}'
