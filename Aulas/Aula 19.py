'''from time import sleep
def contador(i,f,p):
    """
    ->faz uma contagem e mostra na tela.
    i=inicio da contagem
    f=final da contagem
    p=passo da contagem
    return=sem retorno
    """
    if i<f:
        cont = i
        while cont<f:
            cont+=p
            print(f'{cont} ',end='')
            sleep(1/3)
        print('FIM!')
    if i>f:
        cont=i
        while cont>f:
            cont-=p
            print(f'{cont} ',end='')
            sleep(1/3)
        print('FIM!')


contador(0,10,2)
contador(10,0,3)
help(contador)'''



'''def somar(a=0,b=0,c=0):             #PARAMETROS opcionais, ou seja, se
    s=a+b+c                         # n for digitado numero no a b ou c
    print(f'A soma vale {s}')       # o resultado da variavel é 0.


somar(3,5)'''

'''def teste(b):
    global a            # O A de dentro da função vira o valor global
    a=8
    b+=2
    c=3
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a=5
teste(a)
print(f'A fora vale {a}')'''



'''def somar(a=0,b=0,c=0):
    s=a+b+c
    return s

r1=somar(3,6,1)
r2=somar(3,7)
r3=somar(1,2)
print(f'Os resultados foram {r1}, {r2} e {r3}')'''


def fatorial(num=1):
    f=1
    for c in range(num,0,-1):
        f*=c
        print(f)
    return f

n=int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


