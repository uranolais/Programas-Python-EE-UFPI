class Retangulo:
    def __init__(self,comp,largura):
        self.comprimento=comp
        self.largura=largura
    def alteraLados(self,v1,v2):
        self.comprimento=v1
        self.largura=v2
    def retornaLados(self):
        return self.comprimento and self.largura
    def area(self):
        return self.comprimento*self.largura
    def perimetro(self):
        return (self.comprimento*2)+(self.largura*2)
lados=Retangulo(4,3)
print(lados.area())
print(lados.perimetro())
lados.alteraLados(5,6)
print(lados.area())
print(lados.perimetro())


        
