import time
'''as funções SAUDE, FOME E LIMPEZA SERÃO ALTERADAS COM O TEMPO'''
class Tamagotchi:
    def __init__(self,nome,idade):#a fome e a limpeza vão se alterar com o tempo
        self.nome=nome#nome dele
        self.fome=int(100)#fome com porcentagem inicial de 100%(será alterada pela função comer)
        self.tf=time.time()#tempo da fome
        self.saude=int(100)# saude com porcentagem inicial de 100%(será alterada pela função brincar)
        self.ts=time.time()#tempo da saude
        self.idade=int(idade)#idade do Tamagotchi que eu preferi colocar para o úsuario decidir
        self.limpeza=int(100)#limpeza com porcentagem inicial de 100%(será alterada pela função banhar)
        self.tl=time.time()#tempo da limpeza
    def mudarIdade(self,novaidade):#opção para o usuario mudar a idade de seu bichinho
        self.idade=novaidade
    def mudarNome(self,novonome):#opção para o usuario mudar o nome de seu bichinho
        self.nome=novonome
    def humor(self):#humor vai ser a media ponderada entre fome, saude e limpeza
        humor=(2*self.saude+1*self.limpeza+3*self.fome)//6#divisao inteira //
        return humor
    def comer(self,alimento):#Opção que irá alterar a fome
        if self.fome==100:#laço para não permitir que o usuario alimente o bichinho de barriga cheia
            print("\nSeu Tamagotchi já está completamente cheio!")
        if self.fome!=100 and self.fome!=0:#a fome tem que estar entre 100 e 0
            x=self.fome+alimento#nao pode ter mais de "100%" de alimento. por exemplo se só cabe 1, não da pra colocar 2
            if x>100:#se for maior que 100 nao vai caber
                print("\nNão cabe essa quantidade de comida no seu Tamagotchi")
            if x<=100:#se for menor que 100 vai caber, alimenta ele
                self.fome+=alimento#adicionando o alimento
                print("\nSeu Tamagotchi foi alimentado")
            if self.fome<=0:#opção para matar o tamagotchi
                print("\nSinto muito :(, seu Tamagotchi morreu!")
                exit()
    def banhar(self):#opção que irá alterar a limpeza
        if self.limpeza==100:#opção que nao irá permitir banhar mais que o necessario
            print("\nSeu Tamagotchi já está limpo!")
        if self.limpeza!=100 and self.limpeza!=0:#a limpeza tem que estar entre 100 e 0
            self.limpeza=100
            print("\nSeu Tamagotchi banhou")
        if self.limpeza<=0:#opção para matar o Tamagotchi
            print("\nSinto muito :( seu Tamagotchi morreu!")
            exit()
    def mudarLimpeza(self):# a cada 3 segundos ele perde "1%" e quando atingir 5 minutos (300s)se nao tiver feito nada ele morre!
        ti=time.time()#nesse momento
        tf=int(ti-self.tl)#final-inicial
        if tf>=3:#fiz regra de 3, e a cada 3 segundos ele perde 1% como citado anteriormente
            a=tf//3#divisao inteira entre o tempo e os 3segundos para saber a quantidade que será diminuida
            self.limpeza-=(a)#diminuir a quantidade
            self.tl=time.time()#restaurando o tempo para não ter correr o risco de diminuir mais que 1% a cada 3 segundos
            if self.limpeza<=0:#função matar o Tamagotchi
                print("\nSeu Tamagotchi morreu!")
                exit()
        return self.limpeza
    def mudarFome(self):#mesmo principio de limpeza e saude
        ti=time.time()#tempo nesse momento
        tf=int(ti-self.tf)
        if tf>=3:
            a=tf//3
            self.fome-=(a)
            self.tf=time.time()#restaurar
            if self.fome<=0:
                print("\nSeu Tamagotchi morreu!")
                exit()
        return self.fome
    def mudarSaude(self):#mesmo principio de fome e limpeza
        ti=time.time()
        tf=int(ti-self.ts)
        if tf>=3:
            a=tf//3
            self.saude-=(a)
            self.ts=time.time()#restaurar
            if self.saude<=0:
                print("\nSeu Tamagotchi morreu!")
                exit()
        return self.saude
    def brincar(self,tempo):#função que ira alterar a Saude(para cima), fome e limpeza(para baixo)
        x=self.saude+tempo#checando se a saude não irá ultrapassar os 100%
        if x==100:
            print("\nSeu Tamagotchi brincou demais!")
        if x!=100 and x!=0:
            self.saude=100
            ti=time.time()
            tir=ti+tempo#usando o mesmo principio das funções anteriores
            tf1=int(tir-self.tf)
            tf2=int(tir-self.tl)
            if tf1>=3 and tf2>=3:
                a=tf1
                b=tf2
                self.fome-=(a)
                self.limpeza-=(b)
                self.tf=time.time()
                self.tl=time.time()
            print("\nVocê Brincou com seu Tamagotchi!")
        if self.saude<=0:#matar o Tamagotchi
            print("\nSinto muito :( seu Tamagotchi morreu!")
            exit()
    def verificarSaude(self):
        return self.saude
    def verificarHumor(self):
        return self.humor
    def verificarNome(self):
        return self.nome
    def verificarIdade(self):
        return self.idade
print('*'*30)
print(' '*8,'TAMAGOTCHI',' '*8)
print('*'*30)
t=1
while t==1:
    op=int(input('''
Digite (1) caso queira criar um Tamagotchi
Digite (2) caso queira sair do programa
Sua resposta:'''))
    if op==1:
        #inicio=time.time()
        print("\nLembre-se seu bichinho virtual começa com 100% de limpeza, saúde e barriga cheia! Tudo isso será afetado com o tempo e afetará o humor dele. Cuidado para não deixá-lo morrer.")
        nome=str(input("Qual será o nome do seu Tamagotchi?:"))#pedindo o nome
        idade=int(input("Quantos anos seu Tamagotchi tem?:"))#pedindo a idade
        print("_"*30)
        print(' '*12,'MENU',' '*12)
        print('_'*30)
        bicho=Tamagotchi(nome,idade)#colocando o nome e a idade
        print('''
\nDICA: para uma melhor experiencia, acesse o tutorial!''')
        e=17
        while e==17:
            opc=int(input('''
Digite (1) para alimentá-lo
Digite (2) para banhá-lo
Digite (3) para brincar com ele
Digite (4) para mudar sua idade
Digite (5) para mudar o seu nome
Digite (6) para ver o STATUS de seu Tamagotchi
Digite (7) para ver um TUTORIAL
Digite (8) para matar seu Tamagotchi
Sua resposta:'''))
            if opc==1:
                bicho.mudarFome()#atualizar o nivel de fome
                alimento=int(input("Digite quanto de alimento você quer dar para seu Tamagotchi:"))
                bicho.comer(alimento)
                bicho.humor()#sempre tem que recalcular o humor
            if opc==2:
                bicho.mudarLimpeza()#atualizar o nivel da limpeza
                bicho.banhar()
                bicho.humor()
            if opc==3:#atualizar os niveis
                bicho.mudarFome()
                bicho.mudarLimpeza()
                bicho.mudarSaude()
                tempo=int(input("Digite quanto tempo(em segundos)deseja brincar com seu Tamagotchi:"))
                bicho.brincar(tempo)
            if opc==4:#chamando função mudar idade
                novaidade=int(input("Digite a nova idade:"))
                bicho.mudarIdade(novaidade)
            if opc==5:#chamando função mudar nome
                novonome=str(input("Digite o novo nome:"))
                bicho.mudarNome(novonome)
            if opc==6:#STATUS
                print("\nO nome do seu Tamagotchi é:",bicho.verificarNome())
                print("A idade do seu Tamagotchi é:",bicho.verificarIdade())
                print("A taxa de comida(em porcentagem)no estomago de seu Tamagotchi é:",bicho.mudarFome())
                print("A taxa de limpeza(em porcentagem)de seu Tamagotchi é:",bicho.mudarLimpeza())
                print("A taxa de saúde(em porcentagem)de seu Tamagotchi é:",bicho.mudarSaude())
                print("O humor de seu Tamagotchi(em porcentagem)é:",bicho.humor())
            if opc==7:#TUTORIAL
                print('''
TUTORIAL:
O Tamagotchi é um bichindo virtual que tem os atributos Fome, Limpeza, Saúde e por consequencia Humor modificados com o tempo
- A cada 3 segundos o seu Tamagotchi perde 1% desses atributos.
- O  humor  é  calculado  pela  média  ponderada  da  fome,  da  limpeza  e  da 
saúde, sendo que a fome tem peso 3 e a saúde tem peso 2 e a limpeza tem peso 1.
- Seu Tamagotchi começa com 100% de limpeza 100% de saúde e barriga cheia!
- Ao brincar você estará modificando a fome, a limpeza e a saúde.
- Esse programa dará a você o menu de opções:
>> Opção (1) você poderá alimentar seu Tamagotchi. Você poderá escolher o quanto de alimento dar para ele!
Mas lembre-se que o seu Tamagotchi tem um limite (100%) e quando atingi-lo não poderá alimentá-lo naquele momento.
>> Opção (2) você poderá dar banho no seu Tamagotchi e dessa forma voltar a limpeza para 100%.
>> Opção (3) você poderá brincar com ele. Você poderá dizer o tempo que vai brincar e isso irá afetar na fome,
limpeza, saude e por consequencia humor dele.
>> Opção (4) você pode mudar a idade que você deu a seu Tamagotchi.
>> Opção (5) você poderá mudar o nome de seu Tamagotchi.
>> Opção (6) você terá acesso ao STATUS de seu Tamagochi. O status irá informar todas as taxas nome e idade de seu Tamagotchi.
Em ordem: NOME, IDADE, FOME, LIMPEZA, SAÚDE, HUMOR
>> Opção (7) você terá acesso a esse tutorial.
>> Opção (8) você poderá sair de seu Tamagotchi
Desvantagens: Ele irá morrer e você perderá direito de usar ele e ter suas informações
Vantagens: Você sairá e poderá criar outro Tamagotchi.
ESPERO TER AJUDADO!

Ainda tem duvidas sobre o funcionamento do programa? Envie-me um email: laisbup@hotmail.com
Criadora: Laís Brito Urano Portela. 2017.''')
            if opc==8:#SAIR DO TAMAGOTCHI
                c=int(input('''
Certeza que deseja matar seu Tamagotchi?
Lembre-se que ao matá-lo perderá todas as informações sobre ele :(
Contudo, poderá criar outro Tamagotchi :)
Digite (1) para sim e (2) para não
Sua resposta:'''))
                if c==1:
                    print("\nObrigado por ter jogado! Seu Tamagotchi está morto")
                    e=1#quebrar o while
                if c==2:
                    print("\nContinue a jogar a qualquer momento!")
    if op==2:#SAIR DO PROGRAMA
        exit()
                

