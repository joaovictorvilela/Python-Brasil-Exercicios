tabuada = int(input('Montar um tabuada de: '))
inicio = int(input('Começa por: '))
fim = int(input('Termina em: '))
print(f'Vou montar um tabuada de {tabuada} começando em {inicio} e terminado em {fim}:')

for x in range(inicio,fim+1):
    print(f'{tabuada} x {x} = {tabuada*x}')
