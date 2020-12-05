import random

dado = [0] * 6

for i in range(100):
    lancamento = random.randint(0, 5)
    dado[lancamento] += 1

for i in range(6):
    print(f'{i+1} - {dado[i]}')
