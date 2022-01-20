#LAIS BRITO URANO PORTELA
'''4.  Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As 
perguntas são(2,0 pontos): 
a.  "Telefonou para a vítima?" 
b.  "Esteve no local do crime?" 
c.  "Mora perto da vítima?" 
d.  "Devia para a vítima?" 
e.  "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela 
deve  ser  classificada  como  "Suspeita",  entre  3  e  4  como  "Cúmplice"  e  5  como "Assassino". Caso contrário, ele será classificado como "Inocente" '''
print("responda as questoes com sim ou não:")
v=[]
s=0#contador de sim
v.append(input("você telefonou para a vitima? "))
v.append(input("você esteve no local do crime? "))
v.append(input("você mora perto da vítima? "))
v.append(input("você devia para a vítima? "))
v.append(input("você ja trabalhou com a vitima? "))
print(v)
if v[0]=="sim": #para cada caso está sendo avaliado
    s=s+1
if v[1]=="sim":
    s=s+1
if v[2]=="sim":
    s=s+1
if v[3]=="sim":
    s=s+1
if v[4]=="sim":
    s=s+1
print("a quantidade de sim é:",s)
if s<2:
    print("Você é Inocente")
elif s>=2 and s<=3:
    print("Você é Suspeito")
elif s>3 and s<=4:
    print("Você é Cúmplice")
elif s==5:
    print("Você é o Assassino")
