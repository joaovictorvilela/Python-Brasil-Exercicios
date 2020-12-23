def ContaDigito(numero):
    contador = 0
    if numero.isdigit(): # se o valor for um dígito
        for i in numero: # percorra a string
            contador += 1 # conte os dígitos
        return contador
    return 'Valor inválido na entrada'

def main():
    numero = str(input('Informe um número: ')).strip()
    print(ContaDigito(numero))
main()
