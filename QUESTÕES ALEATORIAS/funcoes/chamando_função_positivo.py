from positivo import ehpositivo
from positivo import negativo
from positivo import ehpar
numero=int(input("Digite um valor:"))
if ehpositivo(numero):
    print("É um numero positivo")
if negativo(numero):
    print("É um numero negativo")
if ehpar(numero):
    print("É um numero par")
else:
    print("É um numero impar")
