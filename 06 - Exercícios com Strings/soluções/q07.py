def contaEspacos(msg):
    espacos = 0
    for caractere in msg:
        if caractere == ' ':
            espacos += 1
    return espacos


def ContaVogal(msg):
    vogal = 0
    for letra in msg:
        if letra in 'aeiou':
            vogal += 1
    return vogal


def main():
    mensagem = str(input('Digite uma mesagem: ')).lower()
    print(f'Nº de espaços: {contaEspacos(mensagem)}')
    print(f'Nº de ocorrências de vogais na mensagem: {ContaVogal(mensagem)}')
main()
