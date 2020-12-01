sexo = str(input('Digite seu sexo F - femino / M - masculino\n>>> ')).upper()

# condições que irá validar a entrada
if sexo == 'F':
    print('Feminino')
elif sexo == 'M':
    print('Maculino')
else:
    print('Opção Inválida')