# pedindo dois valores
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))

# fazendo as comparações para decidir qual é o maior
if n1 < n2:
    for x in range(n1,n2+1):
        print(x,end=' ')
else:
    for x in range(n2,n1+1):
        print(x,end=' ')
