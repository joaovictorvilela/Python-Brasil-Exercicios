def calcularPagamento(valor = 0, dias = 0):
    if valor == 0 and dias > 0:
        return 'Dados inválidos na entrada'
    elif dias == 0:
        return valor
    else:
        return (valor + (valor * 0.03) + (valor * (dias * 0.01)))

def main():
    op = 0
    while True:
        valor = float(input('Digite o valor (em R$): '))
        if valor != 0:
            op += 1
        dias = int(input('Informe a quantidade de dias em atraso: '))
        if valor == 0:
            break
        print(f'Valor total: R${calcularPagamento(valor,dias):.2f}')
        print(f'Operações realizadas: {op}')
main()