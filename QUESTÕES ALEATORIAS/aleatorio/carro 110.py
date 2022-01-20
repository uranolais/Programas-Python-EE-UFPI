# Pergunte  a  velocidade  de  um  carro,  supondo um  valor  inteiro.  Caso  ultrapasse  110  km/h, exiba  uma   mensagem  dizendo  que  o  usuário foi  multado.  Neste  caso,  exiba  o  valor  da multa,  cobrando  R$  5,00  por km  acima  de 110
x=int(input("digite a velocidade do carro"))
if x>110:
    y= 5*(x-110)
    print("você foi mutado com o valor:",y)
