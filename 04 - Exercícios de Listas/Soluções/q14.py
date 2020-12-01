from time import sleep

perguntas = ['Telefonou para a vítima? ','Esteve no local do crime? ','Mora perto da vítima? ','Devia para a vítima? ', 'Já trabalhou com a vítima?',[]]

print('=' * 40)
print(F'{"C.S.I PYTHON3":^40}')
print('=' * 40)
print('Responda as perguntas à seguir com [S/N]\n')

for x in range(0,len(perguntas)-1):
    perguntas[5].append(str(input(f'Você {perguntas[x]} ')))

contador = 0
for respostas in perguntas[5]:
    if respostas.upper() ==  'S':
        contador += 1

classificacao = ''

if contador == 2:
    classificacao = 'SUSPEITO'
elif contador >= 3 and contador <= 4:
    classificacao = 'CÚMPLICE'
elif contador == 5:
    classificacao = 'ASSASSINO'
else:
    classificacao = 'INOCENTE'

print('=' * 40)
print('processando informações...'.upper())
sleep(1)
print(f'Com base em suas respostas, concluímos que você é {classificacao}!\n')
