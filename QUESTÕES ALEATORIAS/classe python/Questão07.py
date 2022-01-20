# 7)
class bombaCombustível:
  def __init__(self,combustível,valor,quantidade): # Digite o combustível entre aspas: A = bombaCombustível ('gasolina',3.20,5600)
    self.tipoCombustível = combustível
    self.valorLitro = valor
    self.quantidadeCombustível = quantidade
  def abastecerPorValor(self,valor):
    litro = valor / self.valorLitro
    self.quantidadeCombustível -= litro
    return litro
  def abastecerPorLitro(self,litro):
    self.quantidadeCombustível -= litro
    return litro * self.valorLitro
  def alterarValor(self,valor):
    self.valorLitro = valor
    return
  def alterarCombustível(self,combustível):
    self.tipoCombustível = combustível
    return
  def alterarQuantidadeCombustível(self,quantidade):
    self.quantidadeCombustível = quantidade
    return
  
# Teste
bomba = bombaCombustível('gasolina',3.6,75000)
print(bomba.tipoCombustível)
print(bomba.valorLitro)
print(bomba.quantidadeCombustível)
print('')
print(bomba.abastecerPorValor(150)) # R$ 150.00
print(bomba.quantidadeCombustível)
print('')
print(bomba.abastecerPorLitro(27)) # 27 litros
print(bomba.quantidadeCombustível)
print('')
bomba.alterarCombustível('etanol')
bomba.alterarValor(4.30)
bomba.alterarQuantidadeCombustível(90000)
print(bomba.tipoCombustível)
print(bomba.valorLitro)
print(bomba.quantidadeCombustível)