'''chave(cpf), nome, idade, telefone.'''
a={}
d={}
print('Digite 1 para as respostas SIM e digite 2 para as respostas NÃO')
print('O CPF não deve vir com o "ponto"')
t=int(input('Você quer criar um contato? '))
while t==1:
    chave=input('Digite o CPF: ')
    d['nome']=input('Digite o nome: ')
    d['idade']=input('Digite a idade: ')
    d['telefone']=input('Digite o telefone: ')
    a[chave]=d
    t=int(input('Você quer criar outro contato? '))
    if t==1:
        d={}
print('ESSA É A SUA AGENDA:')
for key in a.keys(): 
    print('CPF',key,'\n'' NOME:',a[key]['nome'], '\n'' IDADE:',a[key]['idade'],'\n'' TELEFONE:',a[key]['telefone'])

