saltos = ('Primeiro Salto:','Segundo Salto:','Terceiro Salto:','Quarto Salto:','Quinto Salto:')

while True: # usei o while True
    
    nome = str(input('Nome: ')) # pedindo o nome do usuário
    if nome == '': # condição de parada do laço
        break

    contador = 0 # contador para imprimir os saltos na tupla saltos
    lista = [] # lista que vai guardar os saltos dos atletas
    lista.clear() # esvaziando a lista a cada repetição
    while contador < 5:
        lista.append(float(input(f'{saltos[contador]} ')))
        contador += 1

    # calculando a média
    media = maior = menor = 0
    print(f'-=' * 20) # aqui é só para separar o resultado
    print(f'Nome: {nome}') # exibindo o nome do atleta

    for i in range(len(saltos)): # exibindo os saltos
        print(f'{saltos[i]} {lista[i]} m')
        
    print(f'Melhor salto: {max(lista)}') # calculando o maior e menor salto na sequência
    print(f'Pior Salto: {min(lista)}')
    #media = sum(lista) - (max(lista)+min(lista))
    print(f'Média: {sum(lista)/len(lista)}') # calculando a média
    #print(f'Resultado Final: {media}')
    print(f'-=' * 20) # aqui é só para separar o resultado
    