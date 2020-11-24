primeiro_numero = int(input('1º Número: '))
segundo_numero = int(input('2º Número: '))
terceiro_numero = int(input('3º Número: '))

variavel_axiliar = 0

if terceiro_numero < segundo_numero:
    variavel_axiliar = terceiro_numero
    terceiro_numero = segundo_numero
    segundo_numero = variavel_axiliar

if segundo_numero < primeiro_numero:
    variavel_axiliar = segundo_numero
    segundo_numero = primeiro_numero
    primeiro_numero = variavel_axiliar

if terceiro_numero < segundo_numero:
    variavel_axiliar = terceiro_numero
    terceiro_numero = segundo_numero
    segundo_numero = variavel_axiliar

print(f'{primeiro_numero}\n{segundo_numero}\n{terceiro_numero}')