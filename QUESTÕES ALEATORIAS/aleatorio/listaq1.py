'''1.  Escreva um algoritmo que leia e mostre um vetor de 20 elementos inteiros. A seguir, 
conte quantos valores pares existem no vetor. '''
v=[]
i=1
while i<=20:
    x=int(input("Digite um número inteiro:"))
    v.append(x)
    i=i+1
print(" o vetor é:",v)
p,x=0,0
while x<=19:
    if v[x]%2==0:
        p=p+1
    x=x+1
print("A quantidade de números pares é:",p)


