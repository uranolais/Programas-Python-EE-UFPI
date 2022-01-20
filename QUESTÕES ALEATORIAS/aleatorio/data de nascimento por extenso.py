'''Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do 
usuário e imprima a data com o nome do mês por extenso. '''
dia,mes,ano=input("Digite sua data de nascimento (dd/mm/aaaa):").split('/')
meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
print("você nasceu em %s de %s de %s"%(dia,meses[int(mes)-1],ano))
