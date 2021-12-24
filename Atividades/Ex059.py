from time import sleep
v1=0
v2=0
soma=0
multiplicação=0
maior=0
opcao=0
print('\033[34m=-='*15,'CALCULADORA','=-='*15)
v1=float(input('Digite um valor: '))
v2=float(input('Digite outro valor: '))


while opcao!=5:
    print('\033[31m=-=\033[m' * 30)
    print('''\033[1;32m[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa''')
    print('\033[31m=-='*30)
    print('')
    opcao=int(input('Qual a sua opção? '))
    print('')
    if opcao==1:
        soma = v1 + v2
        print('\033[1;32mA soma entre {} e {} é igual a {}.'.format(v1,v2,soma))
    elif opcao==2:
        multiplicação = v1 * v2
        print(f'\033[1;32mO resultado de {v1} x {v2} é {multiplicação}')
    elif opcao==3:
        if v1>v2:
            maior=v1
            print(f'\033[1;32mO maior numero entre {v1} e {v2} é {maior}')
        else:
            maior=v2
            print(f'\033[1;32mO Maior numero entre {v1} e {v2} é {maior}')
    elif opcao == 4:
        print('\033[1;32m Informe os numeros novamente: ')
        v1=float(input('\033[1mDigite um valor: '))
        v2=float(input('Digite outro valor: '))
    elif opcao ==5:
            print('\033[34mFechando programa....')
            sleep(2)
            print('\033[34mFIM DO PROGRAMA!')
    else:
        print('\033[1;31mOpção INVALIDA, Tente novamente.')
    print(' ')
    print(' ')






































