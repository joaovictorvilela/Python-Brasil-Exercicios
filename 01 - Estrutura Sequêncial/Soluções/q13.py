# recebendo a altura em metros
h = float(input('Altura em (m): '))
# recebendo o sexo do usuário
escolha = str(input('Qual é o seu sexo?\nF - Feminino / M - Masculino\n>>> '))
PesoIdeal = 0
# calculando o peso ideal de acordo com o seu sexo
if escolha in 'Ff':
    PesoIdeal = (62.1 * h) - 44.7
elif escolha in 'Mm':
    PesoIdeal =  (72.7 * h ) - 58
# exibindo as informações 
print(f'Peso Ideal: {PesoIdeal}Kg')
