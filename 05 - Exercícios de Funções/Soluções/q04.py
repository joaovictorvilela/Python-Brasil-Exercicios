def validador_numerico(numero):
    if numero <= 0:
        return 'N'
    else:
        return 'P'

def main():
    numero = float(input('Digite um número qualquer: '))
    print(validador_numerico(numero))
mein()