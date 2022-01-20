v=[35,4,6,1,3,2] #len- tamanho das listas
menor=v[0]
cont=1 #posição
while cont<len(v):
    if menor>=v[cont]:
        menor=v[cont]
        posição=cont
    cont+=1
print("o menor numero é:",menor)
print("a posição dele é:",posição)
