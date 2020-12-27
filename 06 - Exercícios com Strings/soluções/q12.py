def valida(numero):
    if '-' in numero:
        temp = numero.replace('-','')
        if len(temp) == 7:
            print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
            return '3' + temp[:3] + '-' + temp[3:]
    else:
        if len(numero) == 7:
            print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
            return '3' + numero[:3] + numero[3:]
        else:
            return numero

def main():
    num = str(input('Telefone: ')).strip()
    print(valida(num))
main()