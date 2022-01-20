''' Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos 
que: 
a.  Possua uma classe chamada bombaCombustível, com no mínimo esses atributos: 
i.  tipoCombustivel. 
ii.  valorLitro 
iii.  quantidadeCombustivel 
b.  Possua no mínimo esses métodos: 
i.  abastecerPorValor(  )  –  método  onde  é  informado  o  valor  a  ser  abastecido  e 
mostra a quantidade de litros que foi colocada no veículo
ii.  abastecerPorLitro(  )  –  método  onde  é  informado  a  quantidade  em  litros  de 
combustível e mostra o valor a ser pago pelo cliente. 
iii.  alterarValor( ) – altera o valor do litro do combustível. 
iv.  alterarCombustivel( ) – altera o tipo do combustível. 
v.  alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante 
na bomba. 
OBS:  Sempre  que  acontecer  um  abastecimento  é  necessário  atualizar  a  quantidade  de 
combustível total na bomba. '''
class Bomba:
    def __init__(self,tipo):
        self.tipo=tipo
        self.valor=3 #valor qualquer inicial
        self.quantidade=0#valor inicial da quantidade
    def abastecerPorValor(self,v): #v=valor
        x=self.valor
        a=int(v/x)
        self.quantidade+=a
        return a #v*1 representa um litro, valor por um litro
    def abastecerPorLitro(self,li):#li=litro
        x=self.valor
        a=li*x
        self.quantidade+=li
        return a
    def alteraValor(self,novovalor):
        self.valor=novovalor
        return self.valor
    def alteraCombustivel(self,novotipo):
        self.tipo=novotipo
        return self.tipo
    def alteraQuantidade(self,novaquantidade):
        op=int(input("deseja alterar a quantidade para mais ou para menos?(Digite 1 para mais e 2 para menos):"))
        if op==1:
            self.quantidade+=novaquantidade
        if op==2:
            self.quantidade-=novaquantidade
        return self.quantidade
t=1
ti=str(input("Para começar, digite o tipo de combustivel:"))
while t==1:
    opc=int(input('''O que você deseja fazer?
                 Digite (1), caso queira abastecer o carro por valor
                 Digite (2), caso queira abastecer o carro por litro
                 Digite (3), caso queira mudar o valor do combustivel
                 Digite (4), caso queira mudar o tipo de combustivel
                 Digite (5), caso queira alterar a quantidade de combustivel
                 Digite (6), caso queira abandonar o programa:'''))
    ini=Bomba(ti)
    if opc==1:
        x=int(input("Digite o valor para abastecer o carro:"))
        print("A quantidade de litros por esse valor é",ini.abastecerPorValor(x))
    if opc==2:
        x=int(input("Digite o valor em litros para abastecer o carro:"))
        print("O valor para essa quantidade de litro é",ini.abastecerPorLitro(x))
    if opc==3:
        x=int(input("Digite o novo valor do combustivel:"))
        print("O novo valor é:",ini.alteraValor(x))
    if opc==4:
        x=str(input("Digite o novo tipo de combustivel:"))
        print("O novo combustivel é:",ini.alteraCombustivel(x))
    if opc==5:
        x=int(input("Digite a quantidade de combustivel:"))
        print("A nova quantidade é:",ini.alteraQuantidade(x))
    if opc==6:
        exit()
        
        

            
            
        
    
