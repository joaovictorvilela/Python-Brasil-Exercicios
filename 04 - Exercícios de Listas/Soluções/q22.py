# lista com os defeitos
defeitos = ['necessita da esfera','necessita de limpeza','troca do cabo/conector','quebrado ou inutilizado ']

# mostrando o indice e o problema dos mouses
for i,v in enumerate(defeitos):
    print(f'[{i+1}] - {v.upper()}')

mouse = [0] * 4 # lista com o total de mouses defeituosos
defeito_mouse = 1 # ativando o laço while
while defeito_mouse != 0:
    defeito_mouse = int(input('>>> '))
    if defeito_mouse != 0:
        mouse[defeito_mouse-1] += 1 # somando os defeitos do mouse de cada categoria

tot_mouse = sum(mouse) # total de mouses computados

for i,v in enumerate(defeitos): # mostrando os valores
    print(f'{v} - {mouse[i]} - {mouse[i]*100/tot_mouse}%')
