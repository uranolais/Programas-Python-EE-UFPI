#Considere  a  empresa  de  telefonia  Tchau. Abaixo  de  200  minutos,  a  empresa  cobra  R$0,20  por  minuto.  Entre  200  e  400  minutos,  o preço  é  R$  0,18.  Acima de  400  minutos  o preço  por  minuto  é  R$  0,15.  Calcule  sua  conta de telefone.
x=int(input("digite o valor de minutos:"))
if x<200:
    y=0.2*x
    print(y)
if 200<x<400:
    y=0.18*x
    print(y)
if x>400:
    y=0.16*x
    print(y)
