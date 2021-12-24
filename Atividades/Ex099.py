from time import sleep
def contador(i,f,p):
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if i < f:
        cont=i
        while cont <= f:
            print(f'{cont} ',end='')
            sleep(1 / 4)
            if p == 0:
                p=1
            else:
                cont+=p
        print('FIM!')
    if i > f:
        cont=i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(1 / 4)
            if p==0:
                p=1
            else:
                cont-=p
        print('FIM!')


#PROGRAMA PRINCIPAL
contador(1,10,1)
contador(10,1,2)
print('AGORA é sua vez de personalziar a contagem!')
i=int(input('Inicio: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
contador(i,f,p)





