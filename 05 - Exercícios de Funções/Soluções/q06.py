def converter_horas(hora,minuto):
    """[converter_horas]

    Args:
        hora ([int]): [hora]
        minuto ([int]): [minutos]

    Returns:
        [int]: [retorna a notação de 24 horas para a notação de 12 horas]
    """
    if 0 < hora > 23 or 0 < minuto > 59:  # verificando dados inválidos na entrada
        return 'Valor inválido na entrada' 
    # retornando a hora convertida na notação de 12 horas
    elif hora < 12: 
        if hora == 0: 
            hora = 12
        return f'{hora}:{minuto}'
    else:
        hora -= 12
    return f'{hora}:{minuto}'

# recebendo os valores
hora = int(input('Hora: '))
minuto = int(input('Minutos: '))
# invocando a função
print(converter_horas(hora,minuto))
