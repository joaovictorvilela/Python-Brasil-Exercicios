resposta = 'S'
soma = media = quantidade = 0
while resposta == 'S':
    nota = float(input('Digite a nota: '))
    quantidade += 1
    soma += nota
    resposta = str(input('Quer continuar? S/N: ')).upper()
media = soma / quantidade

print(f'A média das notas informadas é: {media:.2f}')
