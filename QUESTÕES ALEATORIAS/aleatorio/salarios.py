# Faça um Programa que pergunte quanto você  ganha por hora e o número de horas 
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-
#se que são descontados 11% para o Imposto de Renda, 8%  para o  INSS  e 5%  para  o  
#sindicato,  faça  um  programa  que  nos  dê o  salário  bruto,  quanto  pagou  ao  INSS, 
#quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = 
#Salário Líquido. Calcule os  descontos e o salário líquido, conforme a tabela abaixo: 
#a.  + Salário Bruto : R$ 
#b.  - IR (11%) : R$ 
#c.  - INSS (8%) : R$ 
#d.  - Sindicato ( 5%) : R$ 
#e.  = Salário Liquido : R$
h=int(input("digite a quantidade de horas que você trabalha:"))
g=int(input("digite o quanto você ganha por horas"))
salario=h*g
print("seu salario é bruto é",salario)
s=h*g-11/100*h*g-8/100*h*g-5/100*h*g
print("seu salario liquido é:",s)
inss=8/100*h*g
print("o valor pago para o inss é:",inss)
imposto=11/100*h*g
print("o valor pago para o imposto de renda é:", imposto)
sindicato=5/100*h*g
print("o valor pago para o sindicato é",sindicato)
