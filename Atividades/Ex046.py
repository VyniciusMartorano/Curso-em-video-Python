import random
from time import sleep
jogador=''
print('\033[1;34m='*65)
print('                            JOKENPO                ')
while not jogador == 10:
    print('SUAS OPÇÕES:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\n[ 10 ] PARAR DE JOGAR')
    jogador=int(input('Qual a sua jogada?'))
    pc=random.randint(0,2)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5),print('PO!!!')
    print('='*65,'\033[1;32m')
    if jogador == 0 and pc == 1:
        print('Computador jogou PAPEL\nJogador jogou PEDRA','\nCOMPUTADOR VENCE!')
    elif jogador == 1 and pc == 2:
        print('Computador jogou TESOURA\njogador jogou PAPEL','\nCOMPUTADOR VENCE')
    elif jogador == 2 and pc == 0:
        print('Computador jogou PEDRA\njogador jogou TESOURA','\nCOMPUTADOR VENCE')
    elif pc == 0 and jogador == 1:
        print('Computador jogou PEDRA\nJogador jogou PAPEL', '\nJOGADOR VENCE!')
    elif jogador == 2 and pc == 1:
        print('Computador jogou PAPEL\njogador jogou TESOURA', '\nJOGADOR VENCE')
    elif jogador == 0 and pc == 2:
        print('Computador jogou TESOURA\njogador jogou PEDRA', '\nJOGADOR VENCE')
    elif jogador == 1 and pc == 1:
        print('Computador jogou PAPEL\njogador jogou PAPEL','\nEMPATE')
    elif jogador == 0 and pc == 0:
        print(' Computador jogou PEDRA\nJogador jogou PEDRA','\nEMPATE')
    elif jogador == 2 and pc == 2:
        print('Computador jogou TESOURA\nJogador jogou TESOURA','\nEMPATE')
    else:
        ('\033[1;31mJOGADA É INVALIDA,TENTE NOVAMENTE!\033[m')
    print('\033[34m='*65)
print('FIM DE JOGO')















