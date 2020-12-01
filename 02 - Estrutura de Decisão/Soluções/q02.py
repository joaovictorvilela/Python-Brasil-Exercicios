# recebendo um número
n1 = float(input('Digite um número: '))
# se ele for positivo (maior que 0)
if n1 > 0:
    print(f'O número {n1} é positivo')
# se ele for neutro (igual a 0)
elif n1 == 0:
    print(f'O número {n1} é neutro')
# se ele for negativo (menor que 0)
elif n1 < 0:
    print(f'O número {n1} é negativo')