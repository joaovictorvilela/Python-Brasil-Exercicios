# cabeçalho do programa
print('=' * 60)
print(f'{"Projeção de gastos com abono":^60}')
print('=' * 60)

# variável que irá validar o laço while
salario = 1
# valor do abono,menor abono e soma do abono zeradas
abono = menor_aborno = soma_abono = 0
# listas com os abonos e salarios
abonos = []
salarios = []

# laço para pedir os salário (O LAÇO PARA QUANDO É INFORMADO UM VALOR > 0 OU < 0)
while salario > 0:
    salario = float(input('Salário (0=fim): '))
    if salario > 0:
        salarios.append(salario)
        # calculando o abono de cada salário (20%)
        abono = salario * 0.2
        # if o abono for <= 100, o abono receberá o valor 100
        if abono <= 100:
            # contando as ocorrências dessa condição
            menor_aborno += 1
            abono = 100
        # somando o total do abono
        soma_abono += abono
        # adicionando cada abono na lista
        abonos.append(abono)

# cabeçalho do resultado
print('-' * 60)
print(f'{"Salário (em R$):":^10} {"Abono (em R$)":^20} {"Salário+Abono (em R$)":^20}')
print('-' * 60)

# printando os valores e somando o abono + salario em cada posição
for i,v in enumerate(salarios):
    print(f'{v:<10.2f} {abonos[i]:^30.2f} {v+abonos[i]:^20.2f}')
print('-' * 60)
# mostrando a quantidade de usuário do sistema, soma do abono e quantidade de abonos <= 100
print(f'Quantidade de usuário na seção: {len(salarios)}')
print(f'Valor total gasto com abono: R$ {soma_abono}')
print(f'Funcionário com abono mínimo: {menor_aborno}')
