def somar(n1 = 0, n2 = 0, n3 = 0): # função somar, com 3 parâmetros opcionais, caso o usuário deseje somar apenas 2 valores
    resultado = n1 + n2 + n3 # soma dos valores
    return f'A soma vale {resultado}.' # retorno da soma

def main():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    n3 = int(input('Digite o último número: '))

    print(somar(n1,n2,n3))
main()
