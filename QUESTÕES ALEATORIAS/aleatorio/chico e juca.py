#Chico tem 1,50m e cresce 2 cm por ano, enquanto Juca tem 1,10m e cresce 3 cm por ano. Faça um programa que calcule e imprima quantos anos serão necessários para que Juca seja maior que Chico
x=0
c=1.5
j=1.1
while c>j:
    c=c+0.02
    j=j+0.03
    x=x+1
print("a quantidade de anos é:",x)
