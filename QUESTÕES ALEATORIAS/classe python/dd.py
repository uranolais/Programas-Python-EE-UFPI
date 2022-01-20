class Macaco:
    def __init__(self,nome1,nome2):
        self.nome1=nome1
        self.nome2=nome2
        self.bucho1=[]
        self.bucho2=[]
    def comer(self,nome3,comida):
        if nome3==self.nome1:
            self.bucho1.append(comida)
        else:
            self.bucho2.append(comida)
    def verbucho(self,nome4):
        if nome4==(self.nome1):
            if self.bucho1==[]:
                return 'o bucho do %s está vazio.'%self.nome1
            else:
                for k in range(len(self.bucho1)):
                    return self.bucho1[k]
        if nome4==self.nome2:
            if self.bucho2==[]:
                return 'o bucho do %s está vazio.'%self.nome2
            else:
                for k in range(len(self.bucho2)):
                    return self.bucho2[k]
    def digerir(self,nome5):
        if nome5==self.nome1:
            if self.bucho1==[]:
                return 'o bucho do %s está vazio.'%self.nome1
            else:
                self.bucho1=[]
                return 'a comida do %s foi digerida.'%self.nome1
        else:
            if self.bucho2 == []:
                return 'o bucho do %s está vazio.' % self.nome2
            else:
                self.bucho2 = []
                return 'a comida do %s foi digerida.' % self.nome2
class Macaco2(Macaco):
    def __init__(self,nome,nome2):
        Macaco.__init__(self,nome)

print('CRIANDO SEUS MACACOS!')
print('Crie o seus dois macacos!')
nome1=input('digite o nome do seu primeiro macaco: ')
nome2=input('digite o nome do seu segundo macaco: ')
m=Macaco(nome1,nome2)
def COMIDA():
    nome=input('digite o nome do macaco que você quer alimentar: ')
    comida=input('digite a comida: ')
    print('o macaco %s comeu %s'%(nome,comida))
def DIGERIR():
    nome = input('digite o nome do macaco que você quer alimentar: ')
    print(m.digerir(nome))
def VER():
    nome = input('digite o nome do macaco que você quer alimentar: ')
    print(m.verbucho(nome))

opcoes = {1:COMIDA,
          2:DIGERIR,
          3:VER,
          }
x==0
while x==0:
    x = int(input('''o que você deseja fazer? Escolha sua opção:
            1.Alimentar um dos macacos. 
            2.Digerir comida de um dos macacos.
            3.Ver bucho de um dos macacos.
            4.Matar macacos. (Finaliza o aplicativo)'''))
    if x==4:
        print('os macacos foram mortos.')
        break
    opcoes[x]()