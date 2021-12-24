from random import randint
from time import sleep
from operator import itemgetter
valores={'jogador1': randint(1,6),
         'jogador2': randint(1,6),
         'jogador3': randint(1,6),
         'jogador4': randint(1,6)}
for k, v in valores.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1/2)
print('='*35)
print('Ranking dos jogadores:')
ranking = sorted(valores.items(), key=itemgetter(1), reverse=True)
for c in range(0,4):
    print(f'{c+1} lugar: {ranking[c][0]} com {ranking[c][1]}')