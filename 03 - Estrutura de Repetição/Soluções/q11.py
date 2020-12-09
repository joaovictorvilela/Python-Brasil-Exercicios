# pedindo os valores para o usuário
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
soma = 0
# verificando o intervalo digitado, se o N1 < N2
if n1 < n2:
    for x in range(n1,n2+1):
        print(x,end=' ')
        soma += x
else:
    for x in range(n2,n1+1):
        print(x,end=' ')
        soma += x
print(f'\nSoma: {soma}')