ano = int(input('Digite um ano: '))
# fórmula do ano bissexto
print('É BISSEXTO' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else 'NÃO É BISSEXTO')
