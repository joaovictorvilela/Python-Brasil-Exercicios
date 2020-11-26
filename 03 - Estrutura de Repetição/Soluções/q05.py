populacaoA = 0
crescimentoA = 0

while (populacaoA <= 0):
    populacaoA = int(input('Informe a populacao do pais A: '))
    if (populacaoA <= 0):
        print('Populacao deve ser um valor positivo')
while (crescimentoA <= 0):
    crescimentoA = float(input('Informe o percentual de crescimento do pais A: '))
    if (crescimentoA <= 0):
        print('Percentual de crescimento deve ser um valor positivo')
populacaoB = populacaoA
while (populacaoB <= populacaoA):
    populacaoB = int(input('Informe a populacao do pais B: '))
    if (populacaoB <= populacaoA):
        print('Populacao do pais B deve ser maior que a populacao do pais A')
crescimentoB = crescimentoA
while (crescimentoB >= crescimentoA):
    crescimentoB = float(input('Informe o percentual de crescimento do pais B: '))
    if (crescimentoB >= crescimentoA):
        print('Percentual de crescimento do pais B deve ser menor que o do pais A')

crescimentoA = 1 + (crescimentoA / 100.0)
crescimentoB = 1 + (crescimentoB / 100.0)

ano = 1
while (populacaoA <= populacaoB):
    populacaoA *= crescimentoA
    populacaoB *= crescimentoB
    ano += 1

print(f'{ano} anos para a População do País A ultrapasse a população do País B')
