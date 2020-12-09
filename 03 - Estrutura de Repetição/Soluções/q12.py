numero = int(input('Informe um número para ver sua tabuada: ')) # pedindo um número para o usuário
for i in range(1,11): # fazendo um for para 10 números
    print(f'{numero} x {i} = {i*numero}') # imprimindo o numero, valor de i no laço, i * número


# outra maneira de fazer esse exercício

#c = 1 ---> contador incialmente com valor 1
#while c <= 10: -----> enquanto contador for menor ou igual a 10
#    print(f'{numero} x {c} = {c*numero}') -----> print o numero,contador, contador * numero
#    c += 1 -----> somando um ao contador para evitar laço infinito