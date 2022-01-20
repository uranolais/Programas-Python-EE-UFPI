'''Leia um arquivo mensagem.txt e grave cripto.txt com 
todas as vogais trocadas por ‘*’ '''
texto=open('C:\\Users\\Laís Urano\\Documents\\palavras.txt','r')
saida=open('C:\\Users\\Laís Urano\\Documents\\cripto.txt','w')
for linha in texto.readlines():
    for letra in linha:
        if letra in 'aeiou':
            saida.write('*')
        else:
            saida.write(letra)
texto.close()
saida.close()
    
