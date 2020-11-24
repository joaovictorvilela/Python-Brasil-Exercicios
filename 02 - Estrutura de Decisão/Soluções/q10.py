turno = str(input('[V] - Vespertino\n[M] - Matutino\n[N] - Noturno\nEm que turno você estuda? ')).upper()

saudacao = ''
if turno == 'N':
    saudacao = 'Boa noite!'
elif turno == 'M':
    saudacao = 'Bom dia!'
elif turno == 'V':
    saudacao = 'Boa tarde'
else:
    saudacao = 'opção inválida'
print(saudacao)