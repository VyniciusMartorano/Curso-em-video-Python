cont=0
s=0
for c in range(1,7):
    n=int(input('Digite o {}° valor:'.format(c)))
    if n%2==0:
        s = s + n
        cont=cont+1
print('Você informou {}° numeros PARES  e a soma foi {}'.format(cont,s))

