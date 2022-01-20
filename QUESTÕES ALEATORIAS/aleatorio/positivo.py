# Escreva  um    programa  que  leia  números  enquanto  forem  positivos  e  imprima  quantos números foram digitados.
i=0
x=1
while x>0:
    x=int(input("Digite um numéro inteiro:"))
    #if x<=0:
        #break
    i=i+1
if x<=0:
    i=i-1
print("a quantidade de numeros positivos é:",i)
