def zero():
    print("você digitou zero\n")

def sqr():
    print("n é um quadrado perfeito\n")

def even():
    print("n é par\n")

def prime():
    print("n é primo\n")
options=(0==zero,1==sqr,4==sqr,2==even,3==prime,5==prime,7==prime)
print("Escolha uma opção:")
num=int(input(1))
options[num]()
