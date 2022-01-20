''' Escreva uma função que recebe as 3 notas de um aluno por parâmetro e uma 
letra. Se a letra for A a função calcula a média aritmética das notas do aluno, se 
for  P,  a  sua  média  ponderada  (pesos:  5,  3  e  2)  e  se  for  H,  a  sua  média 
harmônica(número  de  valores  dividido  pela  soma  do  inverso  dos  valores).  A 
média calculada deve ser retornada pela função.'''

def media(x,y,z,letra): #notas e letra é o parametro
    if letra=="A":
        media=(x+y+z)/3
    if letra=="P":
        media=(5*x+3*y+2*z)/10
    if letra=="H":
        media=(3/(1/x)+(1/y)+(1/z))
    return media
    
