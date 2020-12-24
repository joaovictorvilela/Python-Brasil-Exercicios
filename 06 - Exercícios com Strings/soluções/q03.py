def imprimir(nome):
    for i in range(len(nome)):
        print(nome[i])

def main():
    n = str(input('Digite seu nome: ')).upper().strip()
    imprimir(n)
main()