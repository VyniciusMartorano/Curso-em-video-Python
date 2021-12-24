'''def continuar():
    continuar=str(input('Quer continuar[S/N]?')).strip().upper()[0]
    while continuar not in 'SN':
        print('ERRO!Digite S ou N.')
        continuar=str(input('Quer continuar[S/N]?')).strip().upper()[0]


def mensagem(msg):
    print('-'*35)
    print(msg)
    print('-'*35)
    print()


mensagem('Sistema de alunos')
mensagem('Cadastre sua nota')
continuar()'''


'''def soma(a, b):
    print(f'A={a} e B={b}')
    soma=a+b
    print(f'A soma {a}+{b}={soma}')


soma(4,5)'''


'''def contador(*num):
    tam=len(num)
    print(f'Recebi os valores {num} e são {tam} numeros ao todo.')


contador(2,6,2,9,45)'''


'''def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1


lista=[1,5,8,3,5]
dobra(lista)
print(lista)'''


def soma(* valores):
    s=0
    for num in valores:
        s+=num
    print(f'Somando os valores {valores} temos {s}.')


soma(5,8,3,6,89,2)








