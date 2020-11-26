# Enfeite do código
print('-='*20)
print('EQUAÇÃO DO 2º GRAU')
print('-='*20)

# Variáveis auxiliares 
a = int(input('Digite o valor de A: '))
if a > 0:
    b = int(input('Digite o valor de B: '))
    c = int(input('Digite o valor de C: '))

    # calculando o delta
    delta = b*b - 4*a*c

    # calculando a raiz
    raiz = delta ** (1/2)

    # Calculando as raízes, 1º caso delta < 0
    if delta < 0:
        print(f'Delta = {delta} - A equação não possuí raízes')
    # 2º caso: delta = 0
    elif delta == 0:
        x = -1 * (b + raiz)/(2*a)
        print(f'Delta = {delta} - A equação possuí apenas uma raíz\nX = {x:.2f}')
    # 3º caso: delta > 0
    elif delta > 0:
        x1 = -1* (b + raiz) / (2 * a)
        x2 = -1* (b - raiz) / (2 * a)
        print(f'Delta = {delta} - A equação possuí  duas raízes\nX1 = {x1:.2f}\nX2 = {x2:.2f}')
else:
    print('Essa raiz não é do 2º grau.')