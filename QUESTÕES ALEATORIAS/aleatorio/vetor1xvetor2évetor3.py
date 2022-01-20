''' Escreva um algoritmo que leia dois vetores de 10 posições e faça a multiplicação dos 
elementos  de  mesmo  índice,  colocando  o  resultado  em  um  terceiro  vetor.  Mostre  o 
vetor resultante. '''
v1=[]
v2=[]
i=0
while i<=9:
    n=int(input("Digite um numero inteiro para o vetor 1:"))
    v1.append(n)
    z=int(input("Digite um numero inteiro para o vetor 2:"))
    v2.append(z)
    i=i+1
print("o vetor 1 é:",v1)
print("o vetor 2 é:",v2)
i=0
v3=[]
while i<=9:
    k=v1[i]*v2[i]
    v3.append(k)
    i+=1
print("o vetor 3 é:",v3)
    
