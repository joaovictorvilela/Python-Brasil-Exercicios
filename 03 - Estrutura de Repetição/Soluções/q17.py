num = int(input('Digite: '))
# pegando o número
result =  1
# variável com valor 1
while num != 0:
    # enquanto o número for diferente de 0
    result *= num
    # multiplique ele por numero
    num -= 1
    # remova um número dele
print(result)