# pegando os valores
n1 = float(input('1º número: '))
n2 = float(input('2º número: '))
n3 = float(input('3º número: '))

# definindo o menor número como o n1
menor = n1

# verificando se ele realmente é o menor
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n2 and n3 < n1:
    menor = n3

print(f'O menor número digitado foi o {menor}')