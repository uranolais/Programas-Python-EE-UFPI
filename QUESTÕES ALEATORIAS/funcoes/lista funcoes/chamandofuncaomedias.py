import funcaomedias
x=input("Digite o valor da primeira nota:")
y=input("Digite o valor da segunda nota:")
z=input("Digite o valor da terceira nota:")
media=str(input("Qual media você quer? Use A para aritmetica, P para ponderada e H para harmonica?:"))
media=media.upper()
print(funcaomedias.media(x,y,z,media))
