'''2.  Escreva um algoritmo que leia dois vetores de 10 posições e faça a multiplicação dos 
elementos  de  mesmo  índice,  colocando  o  resultado  em  um  terceiro  vetor.  Mostre  o 
vetor resultante.'''
v1=[]
v2=[]
vr=[]
x,y,z=1,1,0 #como o vr nao ta pedindo o numero inteiro como os outros começa do 0, ja que o numero inteiro começa do 1, por isso o 10 e o 9
while x<=10:
    v1.append(int(input("digite o valor da primeira matriz:")))
    x=x+1
print("a primeira matriz é:",v1)
while y<=10:
    v2.append(int(input("digite o valor da segunda matriz:")))
    y+=1
print("a segunda matriz é:",v2)
while z<=9:
    vr.append(v1[z]*v2[z])
    z=z+1
print("a matriz resultante é:",vr)
