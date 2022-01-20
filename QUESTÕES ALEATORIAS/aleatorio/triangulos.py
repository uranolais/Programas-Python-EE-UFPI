 #Faça  um  Programa  que  peça  os  três  lados  de  um  triângulo.  O  programa  deverá 
#informar  se  os  valores  podem  ser  um  triângulo.  Indique,  caso  os  lados  formem  um 
#triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
x=int(input("digite o primeiro lado:"))
y=int(input("digite o segundo lado"))
z=int(input("digite o terceiro lado"))
if x>0 and y>0 and z>0:
    print("os lados podem formar um triangulo")
if x==y==z:
    print("triangulo equilatero")
if x!=y!=z:
    print("triangulo escaleno")
if x==y!=z or x==z!=y or x!=z==y:
    print("triangulo isoceles")
