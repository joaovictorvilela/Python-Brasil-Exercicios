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

valida = False
bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
    
# Meses com 31 dias
if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
    if(dia<=31):
        valida = True
# Meses com 30 dias
elif( mes==4 or mes==6 or mes==9 or mes==11):
    if(dia<=30):
        valida = True
elif mes==2:
    # Testa se é bissexto
    if bissexto:
        if (dia<=29):
            valida = True
    elif (dia<=28):
            valida = True

if (valida):
    print('Data válida')
else:
    print('Inválida')
