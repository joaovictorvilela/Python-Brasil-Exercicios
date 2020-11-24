n = int(input('Digite um número: '))

dia = ''

if n == 1:
    dia = 'Domingo'
elif n == 2:
    dia = 'Segunda'
elif n == 3:
    dia = 'Terça'
elif n == 4:
    dia = 'Quarta'
elif n == 5:
    dia = 'Quinta'
elif n == 6:
    dia = 'Sexta'
elif n == 7:
    dia = 'Sábado'
else:
    dia = 'Opção inválida'
print(dia)