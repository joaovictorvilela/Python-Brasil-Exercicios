def print_especial(numero): # função que tem parãmetro um número
    for x in range(1,numero+1): # inciando o for com e indo até o número + 1
        for y in range(1,x+1): # somando um ao x do for anterior
            print(f'{x}',end='') # mostrando o x a lado do outro e pulando uma linha
        print()

numero = int(input('Digite um número: '))
print_especial(numero)