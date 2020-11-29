num = int(input('Digite um número: '))
print('Esses são os números primos dentro do intervalo desejado: ',end='')
for c in range(1,num + 1):
    if num % c == 0:
        print(f'{c}',end='  ')
    
        