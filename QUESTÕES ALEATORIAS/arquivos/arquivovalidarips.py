'''Crie um programa que leia um arquivo texto contendo 
uma série de endereços Ips e faça sua validação. A regra 
de validação é que cada octeto de um endereço deve ser 
um valor de no máximo 255. O progama deverá criar dois 
novos arquivos. Valido.txt que conterá os IPs válidos e 
Invalidos.txt que conterá aqueles endereços que não 
seguem o padrão. '''
def ipok(ip):
    ip=ip.split(".")
    for n in ip:
        if int(n)>255:
            return False
    return True
arquivo=open('C:\\Users\\Laís Urano\\AppData\\Local\\Programs\\Python\\Python36\\arquivos\\ips.txt','r')
validos=open('C:\\Users\\Laís Urano\\AppData\\Local\\Programs\\Python\\Python36\\arquivos\\validos.txt','w')
invalidos=open('C:\\Users\\Laís Urano\\AppData\\Local\\Programs\\Python\\Python36\\arquivos\\invalidos.txt','w')
for linha in arquivo.readlines():
    if ipok(linha):
        validos.write(linha)
    else:
        invalidos.write(linha)
arquivo.close()
validos.close()
invalidos.close()
