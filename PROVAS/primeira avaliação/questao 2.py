#LAIS BRITO URANO PORTELA
'''2.  Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo 
de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: 
  Média de Aproveitamento   Conceito 
  Entre 9.0 e 10.0                         A 
  Entre 7.5 e 9.0                           B 
  Entre 6.0 e 7.5                           C 
  Entre 4.0 e 6.0                           D 
  Entre 4.0 e zero                         E 
 
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem 
“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E(2,0 
pontos).'''
nota1=float(input("Digite o valor da primeira nota:"))
nota2=float(input("Digite o valor da segunda nota:"))
media=(nota1+nota2)/2 
print("Suas notas foram %d e %d" %(nota1,nota2))#o %d faz com que seja mais direta, para não ter que ficar abrindo e fechando strings
print("Sua média é:",media)
if media>9.0 and media<=10.0: #media entre o 9 e o 10, podendo ser 10
    print("Você foi APROVADO com conceito A")
if media>7.5 and media<=9.0: #media entre 7.5 e 9, podendo ser 9
    print("Você foi APROVADO com conceito B")
if media>6.0 and media<=7.5: #media entre 6 e 7.5, podendo ser 7.5
    print("Você foi APROVADO com conceito C")
if media>4.0 and media<=6.0: #media entre 4 e 6, podendo ser 6
    print("Você foi REPROVADO com conceito D")
if media>=0 and media<=4.0: #media entre zero e 4, podendo ser zero e 4
    print("Você foi REPROVADO com conceito E")
    

