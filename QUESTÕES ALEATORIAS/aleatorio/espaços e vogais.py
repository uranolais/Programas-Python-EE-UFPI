'''Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo 
espaços em branco), conte: 
a)  quantos espaços em branco existem na frase. 
b)  quantas vezes aparecem as vogais a, e, i, o, u. '''
frase=input("digite uma frase:")
vogais=0
espaco=0
while vogais<len(frase):
    if frase[vogais] in 'aeiou':
        vogais=vogais+1
        print("a quantidade de vogais é:",vogais)

    espaco+=1
    print("A quantidade de espaços é:",espaço)
    
  
