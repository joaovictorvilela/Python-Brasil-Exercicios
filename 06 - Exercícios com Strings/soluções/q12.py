def valida_numero(numero):
    com_f = '3' + numero[:4] + '-' + numero[4:]
    sem_f = '3' + numero[:4] + numero[4:]
    if len(numero) == 7:
        print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
        return f'Número com formatação: {com_f}\nNúmero sem formatação: {sem_f}'
    else:
        if len(numero) > 8:
            return 'Número inválido!'
        else:
            return numero


def main():
    num = str(input('Telefone: ')).strip().replace('-','')
    print(valida_numero(num))
main()