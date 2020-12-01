# recebendo a letra do usuário e convertendo ela para minúsculo
letra = str(input('Digite um letra: ')).lower()
# definindo se ela é vogal, consoante ou se a entrada é inválida
if letra in 'aeiou':
    print(f'{letra} é vogal')
elif letra in 'bcdfghjklmnpqrstvwxyz':
    print(f'{letra} é consoante')
else:
    print('Dados inválidos')