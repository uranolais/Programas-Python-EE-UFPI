'''Faça um programa que receba do usuario um arquivo texto e um caractere.Mostre na tela quantas vezes aquele caractere ocorre dentro do arquivo'''
texto=open(str(input("Digite o local do arquivo:")),'r')
caractere=input("Digite um caractere:")
c=0
for linha in texto.readlines():
    for letra in linha:
        if letra in caractere:
            c=c+1
print(c)
texto.close()
