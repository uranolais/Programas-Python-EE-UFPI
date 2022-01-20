'''faça um programa que receba do usuario um arquivo texto e mostra na tela quantas vezes cada letra do alfabeto aparece dentro do arquivo'''
def conta(g):
    c=0
    for linha in texto.readlines():
        for letra in linha:
            if g==letra:
                c+=1
    return c
texto=open(str(input("Digite o local do arquivo:")),'r')
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
k=0
while k<len(l):
    print('A letra %s aparece %d vezes'%(l[k],conta(l[k])))
    k+=1
texto.close()
