''' Elaborar  um  algoritmo  que  lê  um  conjunto  de  30  valores  e  os  coloca  em  2  vetores 
conforme os valores forem pares ou ímpares. O tamanho do vetor é de 5 posições. Se 
algum vetor estiver cheio, escrevê-lo. Terminada a leitura escrever o conteúdo dos dois 
vetores. Cada vetor pode ser preenchido tantas vezes quantas for necessário. '''
i=0
v=[]
while i<=29:
    n=int(input("Digite um numero:"))
    v.append(n)
    i+=1
v1=[]
v2=[]
i=0
while i<=29:
    if v[i]%2==0:
        v1.append(v[i])
        if len(v1)==4:
            print("vetor par:",v1)
            del v1[0:5]
    else:
        v2.append(v[i])
        if len(v2)==4:
            print("vetor impar:",v2)
            del v2[0:5]
    i+=1
print("vetor par:",v1)
print("vetor impar:",v2)
