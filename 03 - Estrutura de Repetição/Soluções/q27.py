turmas = int(input('Nº de turmas: '))
media = soma = 0
for x in range(turmas):
    quantidadeDeAlunos = int(input(f'Insira o nº de alunos na {x+1}ª turma: '))
    if quantidadeDeAlunos <= 0 or quantidadeDeAlunos > 40:
        print('Dados inválidos na entrada')
    else:
        soma += quantidadeDeAlunos
media = soma / turmas
print(f'Média por alunos na turma: {media:.2f}')
