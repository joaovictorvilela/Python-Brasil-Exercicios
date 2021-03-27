class ContaInvestimento(object):
    def __init__(self, numero, nome, juros, saldo = 0.0):
        self.numero = numero
        self.nome = nome
        self.juros = juros
        self.saldo = saldo

    def alterarNome(self, nome):
        self.nome = nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def adicionaJuros(self):
        self.saldo += (self.saldo * (self.juros / 100.0))

# TESTE DA CLASSE

conta = ContaInvestimento(100, 'João', 10)
conta.deposito(1000)
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)