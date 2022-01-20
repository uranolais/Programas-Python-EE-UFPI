#programa que conta palavras do texto
import string
arq=open('livro.txt')
texto=arq.read()
arq.close()
texto=texto.lower()
for c in string.punctuation:
    texto=texto.replace(c,' ')
texto=texto.split()

dicionario={}
for p in texto:
    if p not in dicionario:
        dicionario[p]=1
    else:
        dicionario[p]+=1
for ch in dicionario:#chave
    print(ch,': ',dicionario[ch])
print("vai aparece",dicionario["vai"])
