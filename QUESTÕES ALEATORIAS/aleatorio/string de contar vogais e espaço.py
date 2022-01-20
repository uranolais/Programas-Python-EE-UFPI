'''1)  Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo 
espaços em branco), conte: 
a)  quantos espaços em branco existem na frase. 
b)  quantas vezes aparecem as vogais a, e, i, o, u. '''
frase=input("Digite uma frase:")
k=0
cont=0
espaco=0
while k<len(frase):
    if frase[k] in 'aeiou':
        cont+=1
    if frase[k] in ' ':
        espaco+=1
    k+=1
print("A quantidade de vogais é %s"%cont)
print("A quantidade de espaços é %s"%espaco)
