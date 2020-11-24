letra = str(input('Digite um letra: ')).lower()

if letra in 'aeiou':
    print(f'{letra} é vogal')
elif letra in 'bcdfghjklmnpqrstvwxyz':
    print(f'{letra} é consoante')
else:
    print('Dados inválidos')