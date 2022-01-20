'''faça um programa que leia uma palavra e troque as vogais por *'''
palavra=input("Palavra: ")
k=0
troca=""
while k<len(palavra):
    if palavra[k] in "aeiou": #se esse caractere esta dentro da string
        troca=troca+"*"
    else:
        troca=troca+palavra[k]
    k+=1
print("Nova palavra %s" %troca)
