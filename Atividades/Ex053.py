n1=int(input('Primeiro termo:'))
r=int(input('Digite a razão da P.A: '))
n11 = n1 + 10 * r
print('Os primeiros 10 termos dessa P.A são:')
for c in range(n1,n11,r):
    print('\033[34m{}'.format(c),end=',')