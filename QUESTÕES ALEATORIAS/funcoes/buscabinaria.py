L=[3,2,4,5,6,8,9,0]
L.sort()#ordenar o codigo
def buscabin(ele,lista):
    pos=len(lista)//2#divisao inteira
    if ele==lista[pos]:
        return True
    if pos==0:
        return False
    elif ele>lista[pos]:
        return(buscabin(ele,lista[pos+1:]))
    else:
        return(buscabin(ele,lista[:pos]))
    return False
print(buscabin(11,L))
