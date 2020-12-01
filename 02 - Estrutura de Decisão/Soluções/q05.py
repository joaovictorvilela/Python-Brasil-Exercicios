# pegando os valores
n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))

# calculando a média
media = (n1+n2) / 2

# definindo o resultado de aproveitamento do aluno
resultado = ''
if media >= 7 and media < 10:
    resultado = 'Aprovado'
elif media == 10:
    resultado = 'Aprovado com distinção'
elif media < 7:
    resultado = 'Reprovado'
print(f'Média: {media} pontos\nSituação: {resultado}')