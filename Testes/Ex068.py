'''PAR OU IMPAR'''
from random import randint
PAR = jogador = vitoria = venceu = IMPAR = computador = ''
cont = 0
while True:
    numjogador = int(input('Diga um valor:'))
    jogador = str(input('Qual a sua escolha?PAR/IMPAR? ')).upper()[0].strip()
    numcomputador = randint(1, 10)
    soma = numjogador + numcomputador
    if numjogador>0:
        if soma%2==0:
            vitoria = 'P'
        else:
            vitoria= 'I'
    if vitoria=='P':
        venceu='PAR'
    if vitoria=='I':
        venceu='IMPAR'

    print(f'Você jogou {numjogador} e o computador jogou {numcomputador}.Total de {soma} e deu {venceu}.')

    if vitoria==jogador:
        jogador='\033[32mVOCÊ GANHOU\033[m'
        cont+=1
    else:
        jogador='\033[31mCOMPUTADOR GANHOU'
        break
if cont>=2:
    print(jogador)
    print(f'GAME OVER! Você venceu {cont}x.')
if cont < 1:
    print('Infelizmente você não ganhou nenhuma rodada :(, Tente novamente.')



