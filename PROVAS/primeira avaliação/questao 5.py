#LAIS BRITO URANO PORTELA
'''5.  Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido 
pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para 
encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes 
(divisões) executados(2,0 pontos). '''
#um numero primo só pode ser divisivel por 1 e ele mesmo
n=int(input("digite o número inteiro:")) #o numero final
c=0 #constante para contar os número de divisões
p=[] #lista para salvar os números primos
while n>1:
    x=n-1
    while x>1:
        if n%x==0: #nesse caso o número nao é primo porque é divisivel por outro numero alem dele e do '1'
            break
        c+=1
        x-=1
    else:
        p.append(n) #se nao tiver divisao exata com outros numeros, adiciona a lista como numero primo
    n=n-1
print("a quantidade de divisões foi:",c)
print("os numeros primos entre 1 e o numero digitado são:",p)

 
