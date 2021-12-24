num=int(input('Digite o primeiro termo para saber sua P.A: '))
r=int(input('Digite a razão: '))
x=1
termo=num
while x <= 10:
    x=x+1
    termo=termo +r
    print('{},'.format(termo), end='')