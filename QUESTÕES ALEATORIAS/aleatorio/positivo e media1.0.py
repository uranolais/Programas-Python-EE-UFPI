#Escreva  um    programa  que  leia  números  enquanto  forem  positivos  e  imprima  a média dos números digitados.
i=0
x=1
soma=0
while x>0:
    x=int(input("digite o número:"))
    if x<=0:
        break
    i=i+1
    soma=soma+x
    print("a soma é:",soma)
print("a quantidade de numeros inteiros positivos é:",i)
media=soma/i
print("a media dos numeros é:",media)
