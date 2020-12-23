def verifica_data(dia,mes,ano):
    valida = False
    bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
    
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        if(dia <= 31):
            valida = True
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if(dia <= 30):
            valida = True
    elif mes == 2:
        if bissexto:
            if (dia <= 29):
                valida = True
        elif (dia <= 28):
                valida = True

    if (valida):
        return exibe_data(dia, mes, ano)
    else:
        return 'A data não é válida'


def exibe_data(dia,mes,ano):
    meses = ["",'Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

    return f'{dia} de {meses[mes]} de {ano}'


def main():
    data = str(input('Informe uma data do tipo dd/mm/aaaa: '))

    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])

    print(verifica_data(dia,mes,ano))

main()