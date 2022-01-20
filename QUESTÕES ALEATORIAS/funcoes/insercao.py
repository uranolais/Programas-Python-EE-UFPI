def inserçao(A):
    for i in range(1,len(A)): #vai começar a comparar a partir do 1, que é o segundo numero do vetor
        x=A[i]
        j=i-1
        while j>=0 and x<A[j]:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=x

    return A
