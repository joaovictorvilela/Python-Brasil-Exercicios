print('-=' * 20)
print('BANCO PYTHON3')
print('-=' * 20)
dinheiro = float(input('Informe um valor (em R$): '))

total = dinheiro
ced = 100
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'{totced} cédulas de {ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
