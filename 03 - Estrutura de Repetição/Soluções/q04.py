# valores da questão
populacaoA = 80000
crescimentoA = 1.03
populacaoB = 200000
crescimentoB = 1.015

# ano com valor 1
ano = 1
while (populacaoA <= populacaoB):
    # enquanto a Populaão A for menor que a B
    populacaoA *= crescimentoA
    populacaoB *= crescimentoB
    ano += 1

print(f'{ano} anos para a População do País A ultrapasse a população do País B')