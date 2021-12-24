n1=int(input('um valor:'))
n2=int(input('outro valor:'))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
print('a soma entre {} e {} é igual a {}'.format(n1,n2,s))
print('a multiplicaçao entre {} e {} é igual a {}'.format(n1,n2,m))
print('a divisão de \n  {} \n por {} resulta em {}'.format(n1,n2,d),end='      ')
print('o resto da divisao de {} por {} resulta em {}'.format(n1,n2,di))
