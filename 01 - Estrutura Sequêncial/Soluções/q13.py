h = float(input('Altura em (m): '))
escolha = str(input('Qual é o seu sexo?\nF - Feminino / M - Masculino\n>>> '))
PesoIdeal = 0
if escolha in 'Ff':
    PesoIdeal = (62.1 * h) - 44.7
elif escolha in 'Mm':
    PesoIdeal =  (72.7 * h ) - 58
print(f'Peso Ideal: {PesoIdeal}Kg')
