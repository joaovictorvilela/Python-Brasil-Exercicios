nome = 'abc'
while len(nome) <= 3:
    nome = str(input('Nome (maior que 3 caracteres): ')).strip().upper()

idade = -1

while idade < 0 or idade > 150:
    idade = int(input('Informe sua idade (entre 0 e 150): '))

salario = -1

while salario <= 0:
    salario = float(input('Informe seu salário (em R$): '))

sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Informe seu sexo M/F: ')).strip().upper()

EstadoCivil = 'a'
while EstadoCivil not in 'CcSsDdVv':
    EstadoCivil = str(input('Estado Civil: ')).strip()
