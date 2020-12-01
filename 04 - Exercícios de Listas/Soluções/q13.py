meses = ['Janeiro','Feveireo','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

temperaturas = []

for temp in range(0,12):
    temperaturas.append(float(input(f'Insira a temperatura do mês de {meses[temp]}: ')))

medias_das_temperaturas = sum(temperaturas) / len(temperaturas)
print('=' * 70)
print(f'{"Os meses que tiveram temperaturas acima da média anual foram: ":^70}')
print(f'Média anual: {medias_das_temperaturas:.2f}°C')
print('=' * 70)
for posicao,temp in enumerate(temperaturas):
    if temp > medias_das_temperaturas:
        print(f'{meses[posicao].upper():<20} {temp:>10}°C',end=' ')
        print()
print('=' * 70)