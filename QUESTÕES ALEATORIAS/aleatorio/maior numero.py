#Faça um Programa que leia três números e mostre o maior deles
x=int(input("digite o primeiro numero:"))
y=int(input("digite o segundo numero:"))
z=int(input("digite o terceiro numero:"))
if x>y and x>z:
    print(x," é o maior numero")
elif y>z and y>x:
    print(y," é o maior numero")
if z>x and z>y:
    print(z,"é o maior numero")
