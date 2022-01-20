#LAIS BRITO URANO PORTELA
'''3.  Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma 
lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da 
média  anual,  e  em  que  mês  elas  ocorreram  (mostrar  o  mês  por  extenso:  1  –  Janeiro,  2  – 
Fevereiro, . . . ) (2,0 pontos). '''
v=[]
x=0 #x é a quantidade de "casas", é o mês
c=0 #c é o acumulador, que começa do zero
while x<=11: #um ano tem 12 meses, então o maximo de números é 12
    v.append(int(input("Digite a média do mês:")))
    c=c+v[x]
    x+=1 # x+=1 é a mesma coisa que x=x+1, o x é o valor que vai definir a quantidade de casas
    print("A lista da media de cada mês é:",v)
m=c/12 #m=media
print("A média é:",m)
if m<v[0]: #se a media total for menor que a media do primeiro mês
    print("A media do mes 1-janeiro ficou acima da media anual com o valor de:", v[0])
if m<v[1]: #se a media total for menor que a media do segundo mês
    print("A media do mes 2-fevereiro ficou acima da media anual com o valor de:", v[1])
if m<v[2]: #se a media total for menor que a media do terceiro mês
    print("A media do mes 3-março ficou acima da media anual com o valor de:", v[2])
if m<v[3]: #se a media total for menor que a media do quarto mês
    print("A media do mes 4-abril ficou acima da media anual com o valor de:", v[3])
if m<v[4]: #se a media total for menor que a media do quinto mês
    print("A media do mes 5-maio ficou acima da media anual com o valor de:", v[4])
if m<v[5]: #se a media total for menor que a media do sexto mês
    print("A media do mes 6-junho ficou acima da media anual com o valor de:", v[5])
if m<v[6]: #se a media total for menor que a media do setimo mês
    print("A media do mes 7-julho ficou acima da media anual com o valor de:", v[6])
if m<v[7]: #se a media total for menor que a media do oitavo mês
    print("A media do mes 8-agosto ficou acima da media anual com o valor de:", v[7])
if m<v[8]: #se a media total for menor que a media do nono mês
    print("A media do mes 9-setembro ficou acima da media anual com o valor de:", v[8])
if m<v[9]: #se a media total for menor que a media do decimo mês
    print("A media do mes 10-outubro ficou acima da media anual com o valor de:", v[9])
if m<v[10]: #se a media total for menor que a media do decimo primeiro mês
    print("A media do mes 11-novembro ficou acima da media anual com o valor de:", v[10])
if m<v[11]: #se a media total for menor que a media do decimo segundo mês
    print("A media do mes 12-dezembro ficou acima da media anual com o valor de:", v[11])
'''O programa poderia ter sido feito também usando uma lista onde continua todos os meses em strings
\\\\\\\\\\por exemplo: media=['1-janeiro','2-fevereiro',(...)]\\\\\\
Entretanto, queria utilizar os conhecimentos que eu aprendi antes da avaliação, utilizando o 'if' para cada mês.
Apesar de fazer com que o computador trabalhe mais, é a forma que eu encontrei pra fixar meu conhecimento do if.
Por isso, utilizei a lista, while e if nessa questão.'''

    
