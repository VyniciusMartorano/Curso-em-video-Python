from random import randint
a=(randint(0,10))
b=(randint(0,10))
c=(randint(0,10))
d=(randint(0,10))
e=(randint(0,10))
tupla=(a,b,c,d,e)
cont=maior=menor=0
print(tupla)
for cont in range(0,len(tupla)):
    cont+1
    vez=tupla[cont]
    if cont==0:
        maior=vez
        menor=vez
    else:
        if vez>maior:
            maior=vez
        if vez<menor:
            menor=vez
print(f'{maior} é o MAIOR valor.')
print(f'{menor} é o MENOR valor.')
