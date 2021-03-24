class Pessoa(object):
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def Envelhercer(self, anos):
        if (self.idade < 21):
            self.altura += 0.5
        self.idade += anos

    def Engordar(self, peso):
        self.peso += peso

    def Emagrecer(self, peso):
        if (peso <= self.peso):
            self.peso -= peso
    
    def Crescer(self, altura):
        self.altura += altura
