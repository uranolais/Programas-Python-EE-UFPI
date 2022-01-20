#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 
#litro para cada 3 metros quadrados e que a tinta é vendida em  latas  de  18  litros,  que  custam  R$  80,00.  Informe  ao  usuário  a  quantidades  de  latas  de  tinta  a  serem 
#compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
m=int(input("digite a quantidade de metros quadrados a ser pintado:"))
if m%54!=0:#54 é 18x3, sao os metros por latas
    latas=int(m/54)+1
else:
    latas=int(m/54)
print("a quantidade de latas é:",latas)
preço=latas*80
print("o preço a pagar é:",preço)






    
