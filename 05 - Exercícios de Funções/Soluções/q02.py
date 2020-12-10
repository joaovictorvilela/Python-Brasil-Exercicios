def print_especial(numero): # função do print
    """[print_especial]
    Args:
        numero ([inteiro]): [recebe um número inteiro e imprima até a n-ésima linha.
    """
    for x in range(1,numero+1): # começaremos fazendo um for iniciando em 1,até o número escolhido +1 (por causa que iniciamos com 1)
        for y in range(1,x+1): # esse for comecará com um e vai somando um ao x anterior
            print(f'{y}',end='') # mostrando os valores um ao lado do outro e pulando uma linha depois
        print()

numero = int(input('Digite um número: '))
print_especial(numero)