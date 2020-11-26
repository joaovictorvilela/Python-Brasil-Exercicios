n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
operacao = str(input('O que deseja fazer? [ + - * /]\n>>> '))

if operacao == '+':
    resultado = n1 + n2
elif operacao == '-':
    resultado = n1 - n2
elif operacao == '*' or 'x':
    resultado = n1 * n2
elif resultado == '/':
    resultado = n1 / n2

if operacao in '+-*x/':
    print(f'Resultado: {resultado}')
    print('É par' if resultado % 2 == 0 else 'É ímpar')
    print('É positivo' if resultado > 0 else 'É negativo')
    print('É inteiro' if resultado == int(resultado) else 'É real')
else:
    print('Operação inválida')
