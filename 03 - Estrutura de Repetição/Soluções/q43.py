nome_do_prodtuo = ('Cachorro Quente','Bauru Simples','Bauru com ovo','Hambúrguer','Cheeseburguer','Refrigerante')
codigo = (100,101,102,103,104,105)
preco = (1.20,1.30,1.50,1.20,1.30,1.00)

c = 0
print(f'\n{"Lachonete Python3":^50}'.upper())
print('-' * 50)
print(f'{"Produto":<15} {"Código":^15} {"Preço":>15}')
print('-' * 50)
for produto in nome_do_prodtuo:
    print(f'{produto:<15} {codigo[c]:^15} {"R$ " + str(preco[c]):>15}')
    c += 1
print('-' * 50)

resposta = 'S'
acumulador = 0

while resposta == 'S':
    codigo = str(input('Código: '))[-1]
    quantidade = int(input('Quantidade: '))
    acumulador += (preco[int(codigo)] * quantidade)
    resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
    
print(f'Valor total R$: {acumulador:.2f}')
