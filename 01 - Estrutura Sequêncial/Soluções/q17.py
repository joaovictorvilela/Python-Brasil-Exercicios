tamanho = float(input('Quantos m² devem ser pintados? '))

litros = (tamanho / 6.0) * 1.1  
latas = int(litros / 18.0)
galoes = int(litros / 3.6)

if (litros % 18 != 0):
    latas += 1

if (litros % 3.6 != 0):
    galoes += 1

mixLatas = int(litros / 18.0)
mixGaloes = int((litros - (mixLatas * 18.0)) / 3.6)
if ((litros - (mixLatas * 18.0) % 3.6 != 0)):
    mixGaloes += 1

print(f'Latas: {latas} - Valor em R$: {latas*80:.2f}')
print(f'Galões: {galoes} - Valor em R$: {galoes * 25}')
print(f'Latas: {mixLatas} e {mixGaloes} - Valor em R$: {(mixLatas * 80) + (mixGaloes * 25)}')
