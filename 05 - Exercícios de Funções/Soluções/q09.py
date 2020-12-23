def inverso_de_numero(numero):
    if numero.isdigit():
        numero = n.strip().upper().split()
        junto = ''.join(numero)
        inverso = ''
        for i in range(len(junto) -1, -1, -1):
            inverso += junto[i]
        return inverso
    return 'Valor inválido na entrada'

def main():
    n = str(input('Digite: '))
    print(inverso_de_numero(n))
main()
