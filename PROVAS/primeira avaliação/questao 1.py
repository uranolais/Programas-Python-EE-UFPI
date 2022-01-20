#LAIS BRITO URANO PORTELA
'''1.  Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-
Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso(2,0 pontos).'''
#OBS: para anular uma linha ou mais para adicionar um comentário, use # no começo ou '''(3 aspas)no começo e no final.
turno=input("digite qual turno você estuda (use m para matutino, v para vespertino e n para noturno):")
if turno=="m": # o sinal '==' é um sinal de comparação 
    print("Bom Dia!")
elif turno=="v": #elif é um if dentro do else, encurta o tamanho do programa
    print("Boa Tarde!")
elif turno=="n":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
