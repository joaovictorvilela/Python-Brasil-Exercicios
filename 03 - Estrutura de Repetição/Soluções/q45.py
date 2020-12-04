print('-' * 30)
print(f'{"GABARITO - PROFESSOR":^30}')
print('-' * 30)

gabarito_professor = []
for x in range(5):
    gabarito_professor.append(str(input(f'{x+1} - ')))

print('-' * 30)
print(f'{"GABARITO - ALUNO":^30}')
print('-' * 30)

nota = 0
notas = []

while True:
    c = 0
    for x in range(5):
        resposta = str(input(f'{c+1} - '))
        c += 1

        # calculando a nota
        if resposta == gabarito_professor[x]:
            nota += 1 
        
        # zerando o contador
        if c == 5:
            c = 0
    # adicioando a nota na lista
    notas.append(nota)
    # zerando a variável nota
    nota = 0

    resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resposta == 'N':
        break

# aqui eu utilizei funções no python mas você poderia usar um laço para pegar os valores
menor = min(notas)
maior = max(notas)
pessoas = len(notas)
media = sum(notas) / pessoas

print('-' * 30)
print(f'{"RESULTADO":^30}')
print('-' * 30)

print(f'Maior nota: {maior} | Menor nota: {menor}')
print(f'Alunos que usaram o sistema: {pessoas}')
print(f'Média das notas: {media:.2f}')
