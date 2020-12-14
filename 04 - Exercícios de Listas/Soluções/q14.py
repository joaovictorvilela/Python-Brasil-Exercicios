from time import sleep

# lista com as perguntas 
perguntas = ['Telefonou para a vítima? ','Esteve no local do crime? ','Mora perto da vítima? ','Devia para a vítima? ', 'Já trabalhou com a vítima?',[]]

# cabeçalho da questão
print('=' * 40)
print(F'{"C.S.I PYTHON3":^40}')
print('=' * 40)
print('Responda as perguntas à seguir com [S/N]\n')

# percorrendo a lista até a penúltima posição, pois a lista[5] guardará as respostas
for x in range(0,len(perguntas)-1):
    perguntas[5].append(str(input(f'Você {perguntas[x]} ')))
# contador iniciando em zero
contador = 0
# percorrendo a lista na posição que contém as respostas e verificando a quantidade de respostas positivas
for respostas in perguntas[5]:
    if respostas.upper() ==  'S':
        contador += 1

classificacao = ''
# condições para a classificação
if contador == 2:
    classificacao = 'SUSPEITO'
elif contador >= 3 and contador <= 4:
    classificacao = 'CÚMPLICE'
elif contador == 5:
    classificacao = 'ASSASSINO'
else:
    classificacao = 'INOCENTE'

# exibindo os resultados
print('=' * 40)
print('processando informações...'.upper())
sleep(1)
print(f'Com base em suas respostas, concluímos que você é {classificacao}!\n')
