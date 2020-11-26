populacaoA = 80000
crescimentoA = 1.03
populacaoB = 200000
crescimentoB = 1.015

ano = 1
while (populacaoA <= populacaoB):
    populacaoA *= crescimentoA
    populacaoB *= crescimentoB
    ano += 1

print(f'{ano} anos para a População do País A ultrapasse a população do País B')