from tatu3 import Cliente
from tatu3 import Conta, ContaEspecial
joao=Cliente('Joao Da Silva','777-1234')
maria=Cliente('Maria Da Silva','555-4321')
contaj=Conta([joao],1,1000)
contam=ContaEspecial([maria,joao],2,500,1000)
contaj.saque(50)
contam.deposito(300)
contaj.saque(50)
contam.deposito(95.15)
contaj.saque(190)
contam.saque(1500)
contaj.extrato()
contam.extrato()
