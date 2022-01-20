''' Faça um programa que solicite o nome do usuário e imprima-o em formato de escada '''
nome=input("Digite o seu nome:")
k=0
while k<len(nome):
    print(nome[:k+1]) # se fosse em ordem decrescende seria (nome[k:])
    k+=1
