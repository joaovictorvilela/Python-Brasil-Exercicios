def ContaDigito(numero):
    """[ContaDigito]

    Args:
        numero ([string]): [recebe um valor e mostra a quantidade de dígitos]

    Returns:
        [inteiro]: [retorna um valor inteiro correspondente a quantidade de dígitos ou uma mensagem de erro caso seja informado um valor inválido]
    """
    contador = 0
    if numero.isdigit(): # se o valor for um dígito
        for i in numero: # percorra a string
            contador += 1 # conte os dígitos
        return contador
    return 'Valor inválido na entrada'

numero = str(input('Informe um número: ')).strip()
print(ContaDigito(numero))
