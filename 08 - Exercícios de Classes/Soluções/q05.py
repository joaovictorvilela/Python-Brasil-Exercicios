class ContaCorrente(object):
    def __init__(self, nome, NumeroDaConta, saldo = 0):
        self.nome = nome
        self.NumeroDaConta = NumeroDaConta
        self.saldo = saldo

    def Depositar(self, valor):
        self.saldo += valor
        print('Depósito efetuado com sucesso!')
        self.MostrarSaldo()

    def Saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print('Saque efetuado com sucesso!')
            self.MostrarSaldo()
        else:
            print('Valor não disponível para saque!')
            self.MostrarSaldo()

    def AlterarNome(self, Novonome):
        self.nome = Novonome

    # Método Opcional
    def MostrarSaldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')
