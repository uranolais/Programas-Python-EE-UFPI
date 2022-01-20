#Escreva  um    programa  que  leia  números  enquanto  forem  positivos  e  imprima  a média dos números digitados.
i=0
y=i-1
x=1
soma=0
while x>0:
    x=int(input("digite o número inteiro:"))
    i=i+1
    print(i)
if x<=0:
    print(y)
n=y+i
print("a quantidade de numeros inteiros é", i)
soma=soma+x
print("a soma dos numeros é:", soma)
print("a quantidade de numeros positivos é:",n)
media=soma/i
print("a media é:",media)
