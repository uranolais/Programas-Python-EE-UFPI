
'''5)  Classe  Macaco:  Desenvolva  uma  classe  Macaco  que  possua  os  atributos  nome  e  bucho 
(estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou 
teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 
alimentos  diferentes  e  verificando  o conteúdo do  estomago  a  cada  refeição.  Experimente 
fazer com que um macaco coma o outro. É possível criar um macaco canibal? '''
class Macaco1:
    def __init__(self,nome):
        self.nome=nome
        self.bucho=[]
    def comer(self,comida):
        self.bucho.append(comida)
        for op in self.bucho:
            print(op)
    def verBucho(self):
        return self.bucho
    def digerir(self):
        self.bucho.clear()
    def nome(self):
        return self.nome
    
    
    
m1=str(input("Digite o nome do primeiro macaco:"))
m2=str(input("Digite o nome do segundo macaco:"))
mac1=Macaco1(m1)
mac2=Macaco1(m2)
def comer():
    x=str(input("digite o alimento:"))
    y=str(input("digite o alimento:"))
    z=str(input("digite o alimento:"))
    if x!=y and x!=z and z!=x:
        mac1.comer([x])
        mac1.comer([y])
        mac1.comer([z])
    if x==y and x==z:
        q=str(input("digite o alimento:"))
        w=str(input("digite o alimento:"))
        mac1.comer([x])
        mac1.comer([q])
        mac1.comer([w])
    if x!=y and x==z and y!=z:
        w=str(input("digite o alimento:"))
        mac1.comer(['x'])
        mac1.comer(['y'])
        mac1.comer(['w'])
    if x!=z and x==y and z!=y:
        w=str(input("digite o alimento:"))
        mac1.comer(['x'])
        mac1.comer(['w'])
        mac1.comer(['z'])
    if z==y and z!=x and x!=y:
        q=str(input("digite o alimento:"))
        mac1.comer(['x'])
        mac1.comer(['q'])
        mac1.comer(['z'])
def vbucho():
    print(mac1.verBucho())
def digerir():
    print(mac1.digerir())
def macaco2():
    def comerdois():
        mac2.comer([m1])
        print("O macaco 2 comeu o macaco 1")
    def vbuchodois():
        print("Estomago do macaco 2:",mac2.verBucho())
    def digerirdois():
        print(mac2.digerir())
    def sairdois():
        exit(0)
    selecao2={ 1 : comerdois,
               2 : vbuchodois,
               3 : digerirdois,
               0 : sairdois
               }
    e=17
    while e==17:
        opcoes=int(input('''\nDigite (1) caso deseje alimentar o segundo macaco
        Digite (2) caso deseje ver seu bucho
        Digite (3) caso deseje fazer ele digerir
        Digite (0) caso deseje finalizar o programa:'''))
        selecao1[opcoes]()
    
def sair():
    exit(0)
selecao1={ 1 : comer,
           2 : vbucho,
           3 : digerir,
           4 : macaco2,
           0 : sair
           }
e=17
while e==17:
    opcoes=int(input('''Digite (1) caso deseje alimentar o primeiro macaco
Digite (2) caso deseje ver seu bucho
Digite (3) caso deseje fazer ele digerir
Digite (4) caso deseje mexer com outro macaco
Digite (0) caso deseje finalizar o programa:'''))
    selecao1[opcoes]()
        
        
    
    
    

            
        
