'''2)  Classe Quadrado: Crie uma classe que modele um quadrado: 
a)  Atributos: Tamanho do lado 
b)  Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área; '''
class Quadrado:
    def __init__(self,lado):
        self.lado=lado
    def novoLado(self,novolado):
        self.lado=novolado
    def retornaLado(self):
        return self.lado
    def area(self):
        return self.lado*self.lado
ladoA=Quadrado(4)
print(ladoA.retornaLado())
print(ladoA.area())
ladoA.novoLado(5)
print(ladoA.area())
print(ladoA.retornaLado())

    
