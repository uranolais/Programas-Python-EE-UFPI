#TERCEIRA AVALIAÇÃO
#QUESTÃO 1
#LAÍS BRITO URANO PORTELA
class Veiculo:
    def __init__(self,nome,qlm,tanque):
        self.nome=nome#salvar o nome do carro
        self.qlm=qlm#salvar quantos quilometros o carro faz por litro
        self.tanque=tanque#quantos litros é o tanque
        self.gasolina=0#valor inicial é 0
        self.quilometros=0#valor inicial de km rodados é 0, a ser definido pelo usuario
    def andar(self,km):#é a quantidade de quilometros por litro
        op=self.qlm
        x=self.gasolina  
        if self.gasolina==0: #o carro nao pode andar sem gasolina
            print("\n Você não pode andar pois seu carro está sem gasolina! Abasteça-o para continuar.")
        else:
            lg=km/op #litros gastos é igual a quantidade de quilometros rodados pela quantidade de km/l que o carro faz
            if x>=lg:#a gasolina tem que ser maior que a gasolina a ser gasta
                self.gasolina-=lg#ATUALIZANDO A QUANTIDADE DE GASOLINA
                self.quilometros+=km
                print("\n Seu carro andou!")#informar para o usuario que a tarefa foi concluida
            else:
                print("\n Você não tem gasolina o suficiente para o tanto que deseja andar! Abasteça o seu carro para continuar")
    def adicionarGasolina(self,li):#a quantidade de gasolina a ser adicionada é o li
        w=self.tanque
        e=self.gasolina
        i=e+li
        if i<=w:
            self.gasolina+=li #adiconando a quantidade de litros
            print("\n Seu carro foi abastecido com sucesso!")
        if i>w:
            b=int(input('''
\nVocê nao pode abastecer mais do que a capacidade do tanque!
Deseja ver a quantidade de gasolina que já tem?
Digite (1) para SIM e (2) para não:'''))
            if b==1:
                print("\nSUA QUANTIDADE DE GASOLINA É:",self.gasolina)
                print("A CAPACIDADE DO SEU TANQUE É:",self.tanque)
                
    def nivelGasolina(self):
        return self.gasolina
    def mudarTanque(self,novotanque):
        self.tanque=novotanque
    def mudarQuilometragem(self,novaqlm):
        self.qlm=novaqlm
    def mudarNome(self,novonome):
        self.nome=novonome
    def mostrarNome(self):
        return self.nome
    def mostrarKM(self):
        return self.quilometros
    def mostrarTanque(self):
        return self.tanque
    def mostrarKML(self):
        return self.qlm
t=1 #constante qualquer para iniciar o while
while t==1:
    op=int(input('''
Digite (1) caso queira criar um carro
Digite (2) caso queira sair do programa
Sua resposta:'''))
    if op==1:
        v1=str(input("\n Digite o nome do seu carro:"))
        klm=int(input("Quantos quilometros o seu carro faz por um litro (km/L).Obs: só é necessário digitar a quantidade de quilômetros!"))
        tnq=int(input("Qual a capacidade do tanque do seu carro em litros?"))
        carro1=Veiculo(v1,klm,tnq)
        print("\n Lembre-se que no momento de criação do seu carro, a quantidade de gasolina e o número de quilometros andados é '0' (zero)")
        e=17
        while e==17:
            op=int(input('''
Essas são suas opções:
1. Andar
2. Abastecer
3. Verificar STATUS do carro
4. Mudar a KM/L do carro
5. Mudar a capacidade do tanque
6. Mudar o nome do seu carro
7. TUTORIAL
8. Sair desse carro
Qual opção(em número) é a sua?:'''))
            if op==1:
                adr=int(input("Digite a quantidade de km que seu carro vai andar:"))
                x=carro1.andar(adr)
            if op==2:
                ab=int(input("Digite a quantidade de litros a ser inserido no carro:"))
                y=carro1.adicionarGasolina(ab)
            if op==3:
                print("\nO nome do seu carro é:",carro1.mostrarNome())
                print("Seu nivel de gasolina é:", carro1.nivelGasolina())
                print("Você andou(em quilometros):", carro1.mostrarKM())
                print("A capacidade(em L)é:",carro1.mostrarTanque())
                print("A quantidade de quilometros por litro que seu carro faz é:",carro1.mostrarKML())
            if op==4:
                nk=int(input("Digite sua nova quilometragem por litro:"))
                z=carro1.mudarQuilometragem(nk)
            if op==5:
                nt=int(input("Digite a capacidade do novo tanque(em litros):"))
                b=carro1.mudarTanque(nt)
            if op==6:
                nn=str(input("Digite o novo nome do seu carro:"))
                g=carro1.mudarNome(nn)
            if op==7:
                print('''
No momento de criação do seu carro, a quantidade de gasolina e o número de quilometros andados é '0' (zero).
Será disponibilizado a você um menu de opções
-A primeira opção (1) do menu permmite que você ande com o seu carro. Mas lembre-se de abastece-lo primeiro!
-A segunda opção (2) do menu permite que você abasteça o seu carro. Mas lembre-se que só poderá abastecer,
no máximo, a quantidade limite de seu tanque!
-A terceira opção (3) do menu irá mostrar a você seu nivel de gasolina e quanto você andou.
-A quarta opção (4) do meunu irá permitir que você mude a quantidade de QUILOMETROS que seu carro faz
por LITRO.
-A quinta opção (5) do menu irá permitir que você mude a capacidade do seu tanque.
-A sexta opção (6) do menu irá permitir que você mude o nome do seu carro
-A sétima opção (7) do menu será a de ver esse tutorial
-A oitava opção (8) do menu será a de sair do carro. Mas CUIDADO! ao sair, perderá todas as informações
sobre esse carro, porém, poderá criar outro.

ESPERO TER AJUDADO!

Ainda tem duvidas sobre o funcionamento do programa? Envie-me um email: laisbup@hotmail.com
Criadora: Laís Brito Urano Portela. 2017.
''')
            if op==8:
                s=int(input('''
Deseja sair? Lembre-se que suas informações não serão salvas e você perderá o carro :(
Digite (1) para sim e (2) para não:'''))
                if s==1:
                    print("\nOBRIGADO POR TER JOGADO")
                    e=1#quebrar o laço do while para sair dele e voltar a pergunta inicial
                if s==2:
                    print("Continue Jogando!")
        
    if op==2:
        print("Obrigado por ter jogado!")
        exit()
