vetor = [[],[],[]]

for x in range(0,10):
    vetor[0].append(int(input('Digite: ')))
for y in range(0,10):
    vetor[1].append(int(input('Digite: ')))
vetor[2] = vetor[0] + vetor[1]

print(f'Vetores intercalados {vetor[2]}')
