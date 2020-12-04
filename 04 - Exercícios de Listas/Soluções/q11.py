vetor = [[],[],[],[]]

for x in range(0,10):
    vetor[0].append(int(input('Digite: ')))
for y in range(0,10):
    vetor[1].append(int(input('Digite: ')))
for b in range(0,10):
    vetor[2].append(int(input('Digite: ')))

# concatenando os valores
vetor[3] = vetor[0] + vetor[1] + vetor[2]

print(f'Vetores intercalados {vetor[3]}')