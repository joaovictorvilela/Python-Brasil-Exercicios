# recebendo o tamanho do arquivo e a velocidade da internet
tamanho = float(input('Informe o tamanho do arquivo (em MB): '))
velocidade = float(input('Informe a velocidade de sua internet em (Mbps): '))

# calculando o tempo
temp = tamanho / velocidade

# calculando o tempo em minutos 
tempoMin = temp / 60

# exibindo as informações
print(f'O tempo aproximado de download é {tempoMin:.2f} min')