from tatu2 import Cliente
from tatu2 import Conta
joao=Cliente('Joao da Silva','777-1234')
maria=Cliente('Maria da Silva','555-4321')
contaj=Conta([joao],1,1000)
contam=Conta([maria,joao],2,500)
contaj.saque(50)
contam.deposito(300)
contaj.saque(190)
contam.deposito(95.15)
contam.saque(250)
contaj.extrato()
contam.extrato()

