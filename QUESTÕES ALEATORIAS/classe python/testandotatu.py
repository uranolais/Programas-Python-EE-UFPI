from tatu import Cliente
from tatu import Conta
joao=Cliente("João Da Silva","777-1234")
maria=Cliente("Maria Da Silva","555-4321")
print("Nome: %s Telefone: %s"%(joao.nome,joao.telefone))
print("Nome: %s Telefone: %s"%(maria.nome,maria.telefone))
contaj=Conta([joao],1,1000)
contam=Conta([maria],2,500)
contajm=Conta([maria,joao],2,500)
contaj.resumo()
contam.resumo()
contajm.resumo()