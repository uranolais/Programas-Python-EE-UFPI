'''Faça um programa que leia 3 números positivos e imprima a raiz quadrada de cada 
número.  O  programa  deverá  impedir  a  entrada  de  números  negativos  usando  o comando while. '''
p=0
while p<3:
    x=int(input("Digite um numero:"))
    p=p+1
    if x<=0:
        break
    print("raiz quadrada de",x,"é",x**(1/2))
    print("a quantidade de números é:",p)

