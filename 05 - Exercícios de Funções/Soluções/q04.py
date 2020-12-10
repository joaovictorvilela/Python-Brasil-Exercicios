def validador_numerico(numero):
    """[validador_numerico]
    Args:
        numero ([real]): [recebe um valor qualquer]
    Returns:
        [string]: [retorna P se for positivo e N se for menor ou igual a 0]
    """
    if numero <= 0:
        return 'N'
    else:
        return 'P'

numero = float(input('Digite um número qualquer: '))
print(validador_numerico(numero))