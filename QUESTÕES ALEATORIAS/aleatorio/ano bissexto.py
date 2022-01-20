# Determine se um ano é bissexto. Verifique no Google como fazer isso... 
x=int(input("digite o ano:"))
if x%4!=0:
    print(x," nao é um ano bissexto")
else:
    print(x,"é um ano bissexto")
