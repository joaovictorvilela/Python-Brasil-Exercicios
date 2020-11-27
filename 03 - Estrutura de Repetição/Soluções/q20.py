fatorial = 0
while fatorial <= 16:
    fatorial = int(input('Digite: '))
    if fatorial > 16:
        print('Erro')
    else:
        result = 1
        while fatorial != 0:
            result *= fatorial
            fatorial -= 1
        print(result)