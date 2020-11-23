tamanho = float(input('Informe o tamanho do arquivo (em MB): '))
velocidade = float(input('Informe a velocidade de sua internet em (Mbps): '))
temp = tamanho / velocidade
tempoMin = temp / 60
print(f'O tempo aproximado de download é {tempoMin:.2f} min')