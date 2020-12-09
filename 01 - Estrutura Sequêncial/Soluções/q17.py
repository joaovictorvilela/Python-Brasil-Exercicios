area = int(input("Digite o tamanho da área: "))

#Acrescentamos os 10% de folga
area = area*1.1

#Agora vamos arredondar a área da seguinte maneira
excesso = area - int(area) #aqui estamos pegando as casas decimais da area
area = int(area) #Aqui retiramos a parte inteira da area

if excesso > 0:
    area = area + 1 #sempre devemos arredondar para cima

#Vamos calcular o numero de litros necessários para pintar a casa
litros = area//6
if area % 6 > 0:
    litros = litros + 1

print("Litros necessários:", litros,"\n")

print("1) comprar apenas latas de 18 litros")
latas = litros//18
if litros % 18 > 0:
    latas = latas + 1

print("Serão necessárias", latas, "latas")
print("Obteremos", latas*18, "litros")
print("Total: R$", latas*80)

print("\n2)Comprar apenas galões de 4 litros")
galoes = litros//4
if litros % 4 > 0:
    galoes = galoes + 1

print("Serão necessárias", galoes, "galoes")
print("Obteremos", galoes*4, "litros")
print("Total: R$", galoes*25)

#Vamos pensar, o preço total por litro pago nas latas é 80/18 ~ 4.44 R$/L
#enquanto que para o gualão é 25/4 ~ 6.25 R$/L
#portanto é sempre mais vantajoso comprar o máximo de latas possíveis
#e o mínimo de galões, desde que o preço desses galoes não ultrapasse o preço
#de uma lata, isto é, o numero de galoes seja menor ou igual a 3 (R$ 75)
print("\n3)Misturar latas e galões, de forma que o preço seja o menor.")
latas = litros//18
galoes = 0
litros_restantes = litros%18

if litros_restantes <= 3*4:
    #Ou seja o numero de galoes necessarios seja menor do que três
    galoes = litros_restantes // 4
    if litros_restantes % 4 > 0:
        galoes += 1
else:
    latas += 1

print("Serão necessárias", latas, "latas")
print("Serão necessárias", galoes, "galoes")
print("Obteremos", latas*18 + galoes*4, "litros")
print("Total: R$", galoes*25 + latas*80)
