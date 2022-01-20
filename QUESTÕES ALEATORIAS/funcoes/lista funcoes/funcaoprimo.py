''' Faça uma função que recebe por parâmetro um valor inteiro e positivo e retorna 
o valor lógico Verdadeiro caso o valor seja primo e Falso em caso contrário.'''
def primo(n):
    while n>1:
        x=n-1
        while x>1:
            if n%x==0:
                return False
                break    
            while n%x!=0:
                x=x-1
        x=2
        if n%x!=0:
            return True
