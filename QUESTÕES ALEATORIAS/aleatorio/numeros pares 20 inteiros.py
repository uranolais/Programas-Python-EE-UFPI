'''Escreva um algoritmo que leia e mostre um vetor de 20 elementos inteiros. A seguir, 
conte quantos valores pares existem no vetor.'''
v=[]
i=0
while i<=19:
    n=int(input("Digite um numero inteiro:"))
    v.append(n)
    i+=1
print(v)
soma=0
i=0
while i<=19:
    if v[i]%2==0:
        soma+=1
    i+=1
print("A quantidade de numeros pares é:",soma)
    
          
