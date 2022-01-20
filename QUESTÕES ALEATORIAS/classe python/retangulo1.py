'''3)  Classe Retangulo: Crie uma classe que modele um retangulo: 
a)  Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher) 
b)  Métodos:  Mudar  valor  dos  lados,  Retornar  valor  dos  lados,  calcular  Área  e  calcular 
Perímetro; 
c)  Crie  um  programa  que  utilize  esta  classe.  Ele  deve  pedir  ao  usuário  que  informe  as 
medidas de uma sala, as medidas de uma peça de piso e de um rodapé. Depois, deve 
criar objetos para a sala, o piso e o rodapé com as medidas e calcular a quantidade de 
pisos e de rodapés necessárias para o local. '''
class Retangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def mudarLados(self,novabase,novaaltura):
        self.base=novabase
        self.altura=novaaltura
    def retornaLado1(self):
        return self.base
    def retornaLado2(self):
        return self.altura
    def area(self):
        return self.base*self.altura
    def perimetro(self):
        return (self.base*2)+(self.altura*2)
class Piso(Retangulo):
    def __init__(self,base,altura,piso1,piso2,rodape1):
        Retangulo.__init__(self,base,altura)
        self.piso1=piso1
        self.piso2=piso2
        self.rodape1=rodape1#so vai precisar do comprimento
    def qpiso(self):
        p=self.piso1*self.piso2
        s=self.base*self.altura
        if s%p!=0:
            return (s//p)+1
        else:
            return s//p
    def qrodape(self):
        r=(self.base*2)+(self.altura*2)
        r2=self.rodape1
        if r%r2!=0:
            return (r//r2)+1
        else:
            return r//r2
        
        
s1=int(input("Digite a medida do comprimento da sala:"))
s2=int(input("Digite a medida da largura da sala:"))
p1=int(input("Digite a medida do comprimento do piso:"))
p2=int(input("Digite a medida da largura do piso:"))
r1=int(input("Digite a medida do comprimento do rodape:"))
#sala=Retangulo(s1,s2)
piso=Piso(s1,s2,p1,p2,r1)
print(piso.qpiso())
print(piso.qrodape())


