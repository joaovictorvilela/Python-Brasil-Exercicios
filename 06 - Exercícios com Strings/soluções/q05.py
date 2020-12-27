def print_especial(nome): 
    for x in range(len(nome)-1,-1,-1):
        for y in range(0,x+1):
            print(f'{nome[y]}',end='') 
        print()

def main():
    nome = str(input('Digite um número: '))
    print_especial(nome)
main()