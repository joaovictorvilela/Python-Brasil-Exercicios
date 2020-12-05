sistemas_operacionais = ['Windows Server','Unix','Linux','Netware','Mac OS','Outro'] # lista com os sistemas
votos_geral = [0] * 6 # lista que irá guardar o resultado da votação

print('Melhor S.O. para Servidor (opções 1-6)\n')
for i,v in enumerate(sistemas_operacionais):
    print(f'{i+1:<10} {v:^10}')

while True:
    # laço que irá parar o programa principal
    while True:
        # esse laço irá fazer a validação da entrada dos votos
        numero = int(input('\nVoto (0=fim): '))
        if numero >= 0 and numero <= 6:
            # abaixo são os contadores 
            if numero != 0:
                votos_geral[numero-1] += 1 # adicionando os votos
            break
        # print do erro
        print('Por favor, informe um valor entre 1 e 6 ou 0 para sair!')
    # condição de parada do primeiro laço
    if numero == 0:
        break

print('-' * 50) # print do cabeçalho
print(f'{"Melhor S.O. para uso em servidores":^50}\n')
total = sum(votos_geral) # fazendo a contagem dos votos
print(f'{"N°":<5} {"Sistema Operacional":^20} {"Votos":^10} {"%":^15}') # printando as colunas do resultado
print('-' * 50)
for i,v in enumerate(sistemas_operacionais): # printando o resultado dos votos e calculando a porcentagem
    print(f'{i+1:<5} {v:^20} {votos_geral[i]:^10} {(votos_geral[i] * 100) / total:^15.1f}')
# print da linha final
print('-' * 50)
print(f'{"Total":<5} {total:^51}') # resultado da soma dos votos 
