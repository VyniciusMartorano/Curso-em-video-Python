'''PAR OU IMPAR'''
from random import randint
from time import sleep
ganhou=P=I=''

while True:
    tipo=continuar=' '
    jogador=int(input('Diga um valor:'))
    while tipo not in 'PI':
        tipo=str(input('[ P ] PAR\n[ I ] ÍMPAR\nQual a sua escolha? ')).upper()[0].strip()
    numcomputador = randint(1,10)
    soma=jogador+numcomputador
    print(f'Você jogou {jogador} e o computador jogou {numcomputador}.Total de {soma}.')
    if tipo == 'P':
        if soma%2==0:
            print('Você ganhou!')
        if soma%2>0:
            print('Você perdeu!')
    if tipo == 'I':
        if soma % 2 > 0:
            print('Você ganhou!')
        else:
            print('Você perdeu!')
    while continuar not in 'SN':
        continuar=str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if continuar == 'N':
        sleep(3/2)
        print('Fechando o programa...')
        sleep(2)
        print('Finalizado com sucesso!')

        break







