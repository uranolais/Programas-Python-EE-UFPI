def selecao(v):
    for i in range(0,len(v)):
        min=i
        for j in range(i+1,len(V)):
            if v[j]<V[min]:
                min=j
        x=v[i]
        v[1]=v[min]
        v[min]=x
