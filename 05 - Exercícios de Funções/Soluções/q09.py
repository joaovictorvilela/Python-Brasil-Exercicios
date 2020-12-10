def inverso_de_numero(numero):
    """[inverso_de_numero]

    Args:
        numero ([str): [recebe um valor e mostra o inverso]

    Returns:
        [str]: [retorna o o inverso do número lido ou uma msg de erro caso a entrada esteja inválida]
    """
    if numero.isdigit():
        numero = n.strip().upper().split()
        junto = ''.join(numero)
        inverso = ''
        for i in range(len(junto) -1, -1, -1):
            inverso += junto[i]
        return inverso
    return 'Valor inválido na entrada'

n = str(input('Digite: '))
print(inverso_de_numero(n))
