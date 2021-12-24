from random import randint
from time import sleep
numeros=[]


def sorteio():
    print(f'Sorteando os valores: ',end='')
    for c in range(0,5):
        numeros.append(randint(0,10))
        print(f'{numeros[c]} ',end='')
        sleep(1/2)
    print('FIM!')


def somapar():
    soma=0
    for c in numeros:
        if c % 2 == 0:
            soma+=c
    print(f'Somando os valores pares de {numeros}, temos {soma}.')


sorteio()
somapar()