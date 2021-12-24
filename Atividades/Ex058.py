''' Jogo de adivinhação'''
from random import randint
print('\033[1;31m_'*60)
print("                     JOGO DE ADVINHAÇÃO")
print('Tente Advinhar o numero que o computador sorteou.')
comp=randint(1,10)
tent=0
jog=0
while jog!=comp:
    jog=int(input('\033[31mDigite um valor entre 1 e 10: '))
    if jog<comp:
        print('MAIS')
    if jog>comp:
        print('MENOS')
    if jog>10 or jog<1:
        print("\033[31mOPS, você so pode jogar um numero de 1 à 10,Tente novamente!\033[m")
    tent+=1
print('\033[32mPARABÉNS, VOCÊ ACERTOU!')
print('O numero sorteado pelo computador foi {}'.format(comp))
print('Voce tentou {} vezes até acertar o numero.'.format(tent))

print('\033[1;31m_'*60)


















