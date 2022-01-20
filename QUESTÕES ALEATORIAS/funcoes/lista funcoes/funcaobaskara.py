''' Faça uma função que recebe por parâmetro os valores necessários para o cálculo 
da fórmula de baskara e retorna uma lista com as suas raízes, caso seja possível 
calcular. '''
def baskara(a,b,c):
    d=(b**2)-(4*a*c)
    L=[]
    if d<0:
        print("não é possivel calcular as raizes, pois o delta é negativo")
    if d==0:
        L.append(-b/2*a)
        print("as raizes são iguais, pois o delta é zero")
    if d>0:
        L.append(-b+(d**(1/2))//(2*a)) #Duas barras=divisao inteira
        L.append(-b-(d**(1/2))//(2*a))
        print("Os valores das raízes são:",L)
    return L
    
    
