#Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% ao ano, e um país B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao 
#ano,  faça  um  programa  que  calcule  e  imprima  o  tempo  necessário  para  que  a população do país A ultrapasse a população do país B
ano=0
a=5000000
b=7000000
print("Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% ao ano, e um país B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano")
while a<b:
    a=a*1.03
    b=b*1.02
    ano=ano+1
print("a quantidade de anos é:",ano)
