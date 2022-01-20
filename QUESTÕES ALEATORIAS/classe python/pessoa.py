'''4)  Classe Pessoa: Crie uma classe que modele uma pessoa: 
a)  Atributos: nome, idade, peso e altura 
b)  Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que 
nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm 
e acima dos 40 anos deve diminuir 0,5cm. '''
import datetime
class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura
        self.h=[]
        self.anos=[]
    def crescer(self):
        i=datetime.date.today()-self.idade
        anos=int(i.days/365)
        a=0
        while anos<21:
            b=self.altura+0.5
            a+=1
            self.h.append(['altura:',b])
            return b
        while anos>40:
            b=self.altura-0.5
            a+=1
            self.h.append(['altura:',b])
            return b
    def emagrecer(self):
        self.peso -= 1
        return self.peso
    def engordar(self):
        self.peso += 1
        return self.peso
    def envelhecer(self):
        i=datetime.date.today()-self.idade
        anos=int(i.days/365)
        print(anos+1)
maria=Pessoa('Maria',datetime.date(1999,4,9),57,157)
maria.crescer()
maria.emagrecer()
maria.emagrecer()
maria.engordar()
maria.envelhecer()
print(maria.crescer())
print(maria.emagrecer())
print(maria.engordar())
#print(maria)


        

        
        
        
        
