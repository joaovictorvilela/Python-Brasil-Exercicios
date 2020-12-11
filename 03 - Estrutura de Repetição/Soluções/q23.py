N = int(input("Digite o valor de N: "))
div = 0
for i in range(1, N+1):
    primo = True

    j = 2
    while j < i and primo:
        div += 1
        if i % j == 0:
            primo = False
        j += 1

    if primo:
        print(i)

print(f"Fiz {div} divisões")