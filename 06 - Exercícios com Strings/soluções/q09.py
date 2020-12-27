lista_num = []

def formatacao():
    print('-=' * 20)
    print(f'{"VERIFICADOR DE CPF":^40}')
    print('-=' * 20)


def trasformar_em_numero(cpf):
    # coloca os números do cpf na lista como inteiros
    for numeros in cpf:
        if numeros.isdigit():
            lista_num.append(int(numeros))


def verificar_cpf(lista):
    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(lista) != 11 or len(set(lista)) == 1:
        return 'CPF INVÁLIDO' 

    soma = 0
    aux = 10
    for num in lista[0:9]:
        soma += num*aux
        aux -= 1
    if (soma * 10 % 11) % 10 != lista[9]:
        return 'CPF INVÁLIDO' 
    
    soma = 0
    aux = 11
    for num in lista[0:10]:
        soma += num*aux
        aux -= 1
    if (soma * 10 % 11) % 10 != lista[10]:
        return 'CPF INVÁLIDO'
         
    return 'CPF VÁLIDO' 


def main():
    formatacao()
    cpf = str(input('Informe seu CPF: '))
    trasformar_em_numero(cpf)
    print(verificar_cpf(lista_num))
main()

