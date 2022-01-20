'''Faça um programa que receba do usuario um arquivo texto e mostre na tela quantas linhas esse arquivo possui'''

texto=open(str(input('digite o local do arquivo: ')),'r')
c=0
for linha in texto.readlines():
    c+=1
print(c)
texto.close()

    
