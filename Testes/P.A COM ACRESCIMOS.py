num=int(input('Digite o primeiro termo para saber sua P.A: '))
r=int(input('Digite a razão: '))
x=1
termo=num
y=10
while x <= y:
    x=x+1
    termo=termo +r
    print('{},'.format(termo), end='')
    print(' ')
    y =10+ int(input('Você quer mostrar mais quantos termos?'))
    print('{},'.format(termo), end='')
