class Bola: #nao use input nem print
    def __init__(self,cor,circunferencia,material):
        self.cor=cor #esses dois cor sao diferentes, assim como os outros(o do self.x)
        self.circunferencia=circunferencia
        self.material=material
    def trocaCor(self,novacor):
        self.cor=novacor
    def mostraCor(self): #todos os metodos precisam do metodo
        return self.cor
cor1=Bola('azul',2,'plástico')
print(cor1.mostraCor())
cor1.trocaCor("Vermelho")
print(cor1.mostraCor())
cor2=Bola('amarelo',2,'plástico')
print(cor2.mostraCor())

class Quadrado: #começa com letra maiscula
    def __init__(self,tamanho):
        self.lado=tamanho
    def alteraLado(self,valor):
        self.lado=valor
    def retornaLado(self):
        return self.lado
    def area(self):
        return self.lado*self.lado #multiplicando um lado pelo outro
qua=Quadrado(5)
print(qua.area())
qua.alteraLado(12)
print(qua.retornaLado())
print(qua.area())
