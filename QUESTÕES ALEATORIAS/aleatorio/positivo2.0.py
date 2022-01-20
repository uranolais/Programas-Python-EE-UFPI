# Escreva  um    programa  que  leia  números  enquanto  forem  positivos  e  imprima quantos números foram digitados.
i=0
x=1
while x>0:
    x=int(input("Digite um numero inteiro Qualquer:"))
    i=i+1
if x<=0:
    i=i-1
print("A quantidade de numeros positivos digitados é:",i)
