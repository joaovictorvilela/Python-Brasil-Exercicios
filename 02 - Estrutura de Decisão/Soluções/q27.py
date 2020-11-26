morango = float(input('Digite a quantidade de morangos (Kg): '))
maca = float(input('Digite a quantidade de maçãs (Kg): '))

valorMor = 0

if morango <= 5:
    valorMor = morango * 2.50
elif morango > 5:
    valorMor = morango * 2.20

valorMa = 0

if maca <= 5:
    valorMa = maca * 1.80
elif maca > 5:
    valorMa = maca * 1.50

totalfru = morango + maca
totalvalor = valorMor + valorMa

if totalfru > 8 or totalvalor > 25:
    totalvalor = (valorMa+valorMor) - ((valorMor+valorMa) * 0.1)

print(f'Você deverá pagar R$ {totalvalor:.2f}')
