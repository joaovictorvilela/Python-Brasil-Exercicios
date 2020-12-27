def inverter_string(nome):
    lista_letras = []
    for letra in range(len(nome)):
        lista_letras.append(nome[letra])
    
    result = ''

    for letra in range(len(lista_letras)-1,-1,-1):
        result += lista_letras[letra]

    return result
    

def main():
    nome = str(input('Digite seu nome: ')).strip().upper()
    print(inverter_string(nome))
main()