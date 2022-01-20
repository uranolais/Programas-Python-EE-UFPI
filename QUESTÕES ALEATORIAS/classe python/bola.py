'''1)  Classe Bola: Crie uma classe que modele uma bola: 
a)  Atributos: Cor, circunferência, material 
b)  Métodos: trocaCor e mostraCor '''
class Bola:
    def __init__(self,cor,circunferencia,material):
        self.cor=cor
        self.circunferencia=circunferencia
        self.material=material
    def trocaCor(self,novacor):
        self.cor=novacor
    def mostraCor(self):
        return self.cor
cora=Bola('Azul',4,'plastico')#4 é inteiro
print(cora.mostraCor())
cora.trocaCor('Amarelo')
print(cora.mostraCor())
corv=Bola('Vermelho',4,'plastico')
print(corv.mostraCor())

