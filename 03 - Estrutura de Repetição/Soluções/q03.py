nome = 'abc'
# enquanto o tamanho do nome for menor que 3
while len(nome) <= 3:
    nome = str(input('Nome (maior que 3 caracteres): ')).strip().upper()

idade = -1
# enquanro a idade estiver fora do intervalo
while idade < 0 or idade > 150:
    idade = int(input('Informe sua idade (entre 0 e 150): '))

salario = -1
# enquanro o salário for menor que 0
while salario <= 0:
    salario = float(input('Informe seu salário (em R$): '))

# enquanto o sexo for diferente de F e M
sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Informe seu sexo M/F: ')).strip().upper()

# enquanto o estado civil não estiver em C S D V
EstadoCivil = 'a'
while EstadoCivil not in 'CcSsDdVv':
    EstadoCivil = str(input('Estado Civil: ')).strip()
