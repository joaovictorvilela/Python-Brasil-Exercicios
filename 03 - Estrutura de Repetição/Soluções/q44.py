print(f'{"-= Eleições Python3 =-":^40}'.upper())
print(f'[1] - João\n[2] - Jean\n[3] - Cristina\n[4] - Cícero\n[5] - Voto branco\n[6] - Voto nulo\n[0] - Sair')

while True:
    c1 = c2 = c3 = c4 = c5 = c6 = 0
    escolha = int(input('>>> '))
    if escolha == 0:
        break
    else:
        if escolha == 1:
            c1 += 1
        elif escolha == 2:
            c2 += 1
        elif escolha == 3:
            c3 += 1
        elif escolha == 4:
            c4 += 1
        elif escolha == 5:
            c5 += 1
        elif escolha == 6:
            c6 += 1

total_de_votos = c1 = c2 = c3 = c4 = c5 = c6 

print(f'{"-= Resultado -=":^80}'.upper())
print('-' * 80)
print(f'{"Nº":<15} {"Candidato":<15} {"Votos":^14} {"% votos brancos":^15} {"% votos nulos":^15}')
print('-' * 80)
print(f'{"1":<15} {"João":<15} {c1:^14}')
print(f'{"2":<15} {"Jean":<15} {c2:^14}')
print(f'{"3":<15} {"Cristina":<15} {c3:^14}')
print(f'{"4":<15} {"Cícero":<15} {c4:^14}')
print(f'{"5":<15} {"Votos brancos":<15} {c5:^14}')
print(f'{"6":<15} {"Votos nulos":<15} {c6:^14}')
print('-' * 80)
