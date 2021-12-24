from random import randint
from time import sleep
print('='*6,'MEGA SENA DA VIRADA','='*6)
numeros=[]
cache=[]
jogos=int(input('Quantos jogos você deseja gerar? '))
for n in range(1,jogos+1):
    for c in range(1,7):
        sorteio=randint(1,60)
        cache.append(sorteio)
        if cache[n][c]
    numeros.append(cache[:])
    cache.clear()
    numeros.sort()
print('='*6,f'Sorteando {jogos} jogos','='*6)
for pos in range(0,jogos):
    print(f'JOGO {pos+1}: {numeros[pos]}')
    sleep(1/2)
print('='*9,'BOA SORTE','='*9)
