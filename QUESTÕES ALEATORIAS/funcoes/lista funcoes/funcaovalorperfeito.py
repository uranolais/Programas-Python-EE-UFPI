''' Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito 
perfeito quando ele é igual a soma dos seus divisores excetuando ele próprio. 
(Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar 
um valor booleano. '''
def perfeito(n):
    x=1
    c=0
    while x<n:
        if n%x==0:
            c=c+x
            x+=1
        else:
            x+=1
    if c==n:
        return True
    else:
        return False
        

        
        

