'''Faça um programa que receba do usuario um arquivo texto e mostre na tela quantas letras sao vogais e quantas consoantes'''
texto=open(str(input("Digite o local do arquivo:")),'r')
v,c=0,0
for linha in texto.readlines():
    for letra in linha:
        if letra in 'aeiou':
            v=v+1
        else:
            c=c+1
print("O numero de vogais é:",v)
print("O numero de consoantes é:",c)
texto.close()
