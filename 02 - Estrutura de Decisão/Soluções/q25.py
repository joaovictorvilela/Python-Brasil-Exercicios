print('RESPONDA AS PERGUNTAS ABAIXO COM [sim / nao]')
print()

# perguntas para a classificação
Q1 = str(input('Voce telefonou para a vitima? ')).lower()
Q2 = str(input('Voce esteve no local do crime? ')).lower()
Q3 = str(input('Voce mora perto da vitima? ')).lower()
Q4 = str(input('Voce devia para a vitima? ')).lower()
Q5 = str(input('Voce trabalhou para a vitima? ')).lower()

pontuacao = 0

if Q1 == 'sim':
    pontuacao += 1
if Q2 == 'sim':
    pontuacao += 1
if Q3 == 'sim':
    pontuacao += 1
if Q4 == 'sim':
    pontuacao += 1
if Q5 == 'sim':
    pontuacao += 1

# verificando a classificação

classificação = ''

if pontuacao == 2: 
    classificação = 'SUSPEITO'
elif pontuacao >= 3 and pontuacao <= 4:
    classificação = 'CÚMPLICE'
elif pontuacao == 5:
    classificação = 'ASSASSINO'
else:
    classificação = 'INOCENTE'

print(f'Pontuação: {pontuacao}\nClassificação: {classificação}')
