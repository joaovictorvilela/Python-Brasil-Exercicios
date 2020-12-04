from time import sleep

print('=' * 40)
print(f'{"ANALISADOR DE DATAS":^40}')
print(f'{"Informe uma data do tipo dd/mm/aaaa":^40}')
print('=' * 40)
data = str(input('Digite: '))
print(f'\nAnalisando a data...\n')
sleep(1)

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

resultado = ''
bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

if bissexto:
    if mes in (1,3,5,8,10,12):
        if dia <= 0 or dia > 31:
            resultado = 'Data inválida'
        else:
            resultado = 'Data válida'
    if mes in (4,6,7,11):
        if dia <= 0 or dia > 30:
            resultado = 'Data Inválida'
        else:
            resultado = 'Data válida'
    if mes == 2:
        if dia > 29:
            resultado = 'Data Inválida'
        else:
            resultado = 'Data válida'
elif not bissexto:
    if mes in (1,3,5,8,10,12):
        if dia <= 0 or dia > 31:
            resultado = 'Data inválida'
        else:
            resultado = 'Data válida'
    if mes in (4,6,7,11):
        if dia <= 0 or dia > 30:
            resultado = 'Data Inválida'
        else:
            resultado = 'Data válida'
    if mes == 2:
        if dia > 28:
            resultado = 'Data Inválida'
        else:
            resultado = 'Data válida'
    
print(f'A data {data} é {resultado}')
