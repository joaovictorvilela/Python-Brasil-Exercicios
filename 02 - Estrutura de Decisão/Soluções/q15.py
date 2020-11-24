# Enfeite do código
print('-='*20)
print('classificador de triângulo'.upper())
print('-='*20)

# Inserção dos valores correspondentes aos lados do triângulo
r1 = float(input('Medida do 1º lado: '))
r2 = float(input('Medida do 2º lado: '))
r3 = float(input('Medida do 3º lado: '))

# Variáveis auxiliares 
forma = ''
qual = ''

# Condição para validação do triângulo
if r1 < (r2+r3) and r2 < (r3+r1) and r3 < (r1+r2):
    forma = 'Os segmentos FORMAM um Triângulo'
    if r1 == r2 == r3:
        qual = 'Equilátero'
    elif r1 != r2 != r3:
        qual = 'Escaleno'
    else:
        qual = 'Isóceles'
else:
    forma = 'Os segmentos NÃO FORMAM um Triângulo '

print(f'{forma} {qual}')
