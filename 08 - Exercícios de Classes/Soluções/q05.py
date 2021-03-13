class ContaCorrente(object):
    def __init__(self, nome, NumeroDaConta, saldo = 0):
        self.__nome = nome
        self.__NumeroDaConta = NumeroDaConta
        self.__saldo = saldo

    def Depositar(self, valor):
        self.__saldo += valor
        print('Depósito efetuado com sucesso!')
        self.MostrarSaldo()

    def Saque(self, valor):
        if (self.__saldo >= valor):
            self.__saldo -= valor
            print('Saque efetuado com sucesso!')
            self.MostrarSaldo()
        else:
            print('Valor não disponível para saque!')
            self.MostrarSaldo()

    def AlterarNome(self, Novonome):
        self.__nome = Novonome

    # Método Opcional
    def MostrarSaldo(self):
        print(f'Saldo atual: R${self.__saldo:.2f}')
