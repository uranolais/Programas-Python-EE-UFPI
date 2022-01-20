palavra=input("digite palavra:")
k=0
troca=""
while k<len(palavra):
    if palavra[k] in 'aeiou':
        troca=troca+"*"
    else:
        troca=troca+palavra[k]
    k+=1
print("A nova palavra é %s"%troca)
