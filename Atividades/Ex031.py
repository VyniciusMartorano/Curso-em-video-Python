import random
n1=int(input('Digite um numero de 0 a 5: '))
x=[0,1,2,3,4,5]
y=random.choice(x)
print('O numero sorteado foi {}'.format(y))
if n1==y:
    print('Parabens voce acertou o numero em cheio!'.format(y))
else:
    print('Voce errou!')
