class Empregado(object):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def ObterValores(self):
        return f'Nome: {self.nome}\nSalário mensal: R${self.salario:.2f}'
