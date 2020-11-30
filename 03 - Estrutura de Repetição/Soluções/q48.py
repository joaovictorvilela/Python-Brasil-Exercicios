print('='*40)
print(f'{"INVERSO DO NÚMERO":^40}')
print('='*40)
numero = str(input('Digite: ')).strip().split()
junto = ''.join(numero)
inverso = ''
for i in range(len(junto) -1, -1, -1):
    inverso += junto[i]
print(f'{inverso}')