# pegando os três números
primeiro_numero = int(input('1º Número: '))
segundo_numero = int(input('2º Número: '))
terceiro_numero = int(input('3º Número: '))

# nesse exercício vamos precisar de uma variável auxiliar para guardar o valor que será deslocado
variavel_axiliar = 0

# vamos começar comparando o 3 número com o 2
if terceiro_numero < segundo_numero:
    # se o 3 número for menor
    variavel_axiliar = terceiro_numero
    # a variável auxliar guardará esse valor
    terceiro_numero = segundo_numero
    # o 3 número vai ficar sendo o 2 número
    segundo_numero = variavel_axiliar
    # e o segundo número vai ficar sendo o valor que estava na variável auxiliar

# A lógica se repete para os demais casos
if segundo_numero < primeiro_numero:
    variavel_axiliar = segundo_numero
    segundo_numero = primeiro_numero
    primeiro_numero = variavel_axiliar

# perceba que iremos novamente comparar o 3 número com o segundo, verificando se está tudo em ordem
if terceiro_numero < segundo_numero:
    variavel_axiliar = terceiro_numero
    terceiro_numero = segundo_numero
    segundo_numero = variavel_axiliar

print(f'{primeiro_numero}\n{segundo_numero}\n{terceiro_numero}')