class BombaDeCombustivel(object):
    def __init__(self, TipoDeCombustivel, ValorLitro, QuantidadeDeCombustivel):
        self.TipoDeCombustivel = TipoDeCombustivel
        self.ValorLitro = ValorLitro
        self.QuantidadeDeCombustivel = QuantidadeDeCombustivel

    def AbastecerPorValor(self, valor):
        litros_totais = valor / self.ValorLitro
        
        if (litros_totais <= self.QuantidadeDeCombustivel):
            print(f'Total: {litros_totais:.2f}l')

            self.QuantidadeDeCombustivel -= litros_totais

    def AbastecerPorlitro(self, valor):
        litros_totais = valor * self.ValorLitro

        if (litros_totais <= self.QuantidadeDeCombustivel):
            print(f'Total: R$: {litros_totais:.2f}')

            self.QuantidadeDeCombustivel -= litros_totais

    def AlterarValor(self, valor):
        self.ValorLitro = valor


    def AlterarCombustível(self, valor):
        self.TipoDeCombustivel = valor


    def AlterarQuantidade(self, valor):
        self.QuantidadeDeCombustivel = valor
