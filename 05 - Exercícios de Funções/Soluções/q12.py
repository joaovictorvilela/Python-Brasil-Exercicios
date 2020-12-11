from random import shuffle # importando da blibioteca ramdom o módulo shuffle

def embaralhar(palavra): # definindo minha função
    separado = list(palavra) # criando uma variável que guardará a palavra em forma de lista
    shuffle(separado) # embaralhando a palavra com o módulo importado
    palavra_embaralhada = '' # variável com o resultado final
    for i in range(len(separado)): # juntando todas as letras na variável final
        palavra_embaralhada += separado[i] 
    return palavra_embaralhada # retornando o valor final

palavra = str(input('Digite um palavra: ')).strip() # aqui eu quis só mostrar as palavras original
print(f'{palavra.upper()} | {embaralhar(palavra).upper()}')  # um ao lado da outra mas isso é opcional
