def Palidromo(frase):
    msg = frase.strip().upper().split()
    junto = ''.join(msg)
    inverso = ''
    for i in range(len(junto) -1, -1, -1):
        inverso += junto[i]
        
    if inverso == junto:
        return 'É PALÍNDROMO'
    else:
        return 'NÃO É PALÍNDROMO'


def main():
    string = str(input('Digite uma frase: '))
    print(Palidromo(string))
main()