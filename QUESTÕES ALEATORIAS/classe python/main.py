# 6)
class Ponto:
  def __init__(self,x,y):
    self.x = float(x) # round(x,3)
    self.y = float(y) # round(y,3)
  def imprimir_valores(self):
    return self.x,self.y
class Retangulo:
  def __init__(self,largura,altura,ponto):
    self.largura = float(largura) # round(largura,3)
    self.altura = float(altura) # round(altura,3)
    self.ponto = ponto
  def centro(self):
    p = (2*self.ponto.x + self.largura)/2
    q = (2*self.ponto.y + self.altura)/2

    '''
    0        X     M                M - X = largura
    |________|_____|

    0        X     M        N       N - M = X
    |________|_____|________|
  
    0          N/2          N       N / 2 = metade da largura
    |___________|___________|
    
    '''
    return Ponto(p,q).imprimir_valores()
def valores_retangulo():
  return Retangulo(input('Largura = '),input('Altura = '),Ponto(input('\tVertice inferior esquerdo\nAbscissa = '),input('Ordenada = ')))

  '''
  g = input('Largura = ')
  h = input('Altura = ')
  i = input('\tVertice inferior esquerdo\nAbscissa = ')
  j = input('Ordenada = ')
  return Retangulo(g,h,Ponto(i,j)) 
  
  '''
def centro_retangulo():
  global Q
  return Q.centro()
def menu():
  v = input('Escolha uma das opções:\n1) Alterar os valores do retângulo.\n2) Mostrar as coordenadas do centro do retângulo.\n═>')
  print('')
  if v in ['1']:
    global Q 
    Q = valores_retangulo()
    print ('')
    menu()
  elif v in ['2']:
    print('C =', centro_retangulo())
    return
    # Ao invés de return, poderia ser também:
    # print('')
    # menu()
  else:
    return
Q = valores_retangulo()
print('')
menu()