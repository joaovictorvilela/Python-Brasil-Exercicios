# recebendo a entrada do usuário
turno = str(input('[V] - Vespertino\n[M] - Matutino\n[N] - Noturno\nEm que turno você estuda? ')).upper()

# definindo a saudação com o valor inicial vazio
saudacao = ''

# imprimindo  a saudação de acordo com a entrada
if turno == 'N':
    saudacao = 'Boa noite!'
elif turno == 'M':
    saudacao = 'Bom dia!'
elif turno == 'V':
    saudacao = 'Boa tarde'
# se for uma entrada inválida
else:
    saudacao = 'opção inválida'
print(saudacao)