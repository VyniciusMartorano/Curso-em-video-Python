#for c in range(1,10):
#    print('Oi')
#print('FIM')

#CONTAR DE 1 ATE 9
#for c in range(1,10):
#    print(c)


#Contar de 0 ate 10 pulando de 2 em 2
#for c in range(0,11,2):
#    print(c)


#contar de 0 ate o numero da variavel c
#i=int(input('Digite um numero:'))
#for c in range(0,i+1):
#    print(c)



#i=int(input('inicio: '))
#f=int(input('fim: '))
#p=int(input('passo:'))
#for c in range(i,f+1,p):
#    print(c)







#for c in range(0,3):
#    n=float(input('Digite um numero:'))
#    print('O somatorio dos valores é {:.2f}'.format(n))

#s=0
#for c in range(0,3):
#   n=int(input('Digite um valor:'))
#   s=s+n
#print('A soma dos valores é {}'.format(s))



#print('Os numeros pares que estão no intervalo de 1 a 50 são: ')
#for c in range(0,51,2):
#    print(c)



#from time import sleep
#
#for c in range(10,0,-1):
#    sleep(1)
#    print(c)




#x=int(input('digite um numero='))
#print('------------------------------------')
#print('{} x {:2}= {}'.format(x,1,x*1))
#print('{} x {:2}= {} '.format(x,2,x*2))
#print('{} x {:2}= {}'.format(x,3,x*3))
#print('{} x {:2}= {}'.format(x,4,x*4))
#print('{} x {:2}= {}'.format(x,5,x*5))
#print('{} x {:2}= {}'.format(x,6,x*6))
#print('{} x {:2}= {}'.format(x,7,x*7))
#print('{} x {:2}= {}'.format(x,8,x*8))
#print('{} x {:2}= {}'.format(x,9,x*9))
#print('{} x {:2}= {}'.format(x,10,x*10))
#print("-------------------------------------")

#tabuada reduzida
#n=int(input('Digite um numero: '))
#for c in range(1,11):
#    print('{} x {:2}= {}'.format(n, c, n * c))

#cont=0
#s=0
#for c in range(1,7):
#    n=int(input('Digite o {}° valor:'.format(c)))
#    if n%2==0:
#        s = s + n
#        cont=cont+1
#print('Você informou {}° numeros PARES  e a soma foi {}'.format(cont,s))



#n1=int(input('Primeiro termo:'))
#r=int(input('Digite a razão da P.A: '))
#n11 = n1 + 10 * r
#print('Os primeiros 10 termos dessa P.A são:')
#for c in range(n1,n11,r):
#    print('\033[34m{}'.format(c),end=',')



#frase=str(input('Digite uma frase: ')).strip().upper()
#palavras=frase.split()
#junto= ''.join(palavras)
#inverso=''
#for letra in range(len(junto)-1,-1,-1):
#    inverso=inverso+junto[letra]
#print('O inverso de {} é {}'.format(junto,inverso))
#if inverso==junto:
#    print('Temos um palindromo!')
#else:
#    print('A frase não forma um palindromo.')























#palavra=str(input('Digite uma frase: ')).strip().upper()
#separado=palavra.split()
#junto=''.join(separado)
#inverso=''
#for letra in range(len(junto)-1,-1,-1):
#    inverso= inverso+ junto[letra]
#if junto==inverso:
#    print('A frase  pode formar um palindromo!')
#    print('{}, {}'.format(junto,inverso))
#else:
#    print('A frase nao forma PALINDROMO.')






#juntar a frase
#frase=str(input('Digite uma frase:')).strip().lower()
#separada=frase.split()
#junta=''.join(separada)
#print('A frase junta é, {}'.format(junta))



#escrever o inverso da frase
#frase=str(input('Digite uma frase: ')).strip().lower()
#separado=frase.split()
#junto=''.join(separado)
#inverso=''
#for letra in range(len(junto)-1,-1,-1):
#    inverso=inverso +junto[letra]
#print(inverso)




#import datetime

#atual=datetime.date.today().year
#testar=0
#maiores=0
#menores=0
#for pessoa in range(1,8):
#    ano = int(input('Em que ano a {}°pessoa nasceu? '.format(pessoa)))
#    testar=atual-ano
#    if testar>=18:
#        maiores=maiores+1
#    else:
#        menores=menores+1
#print('Ao todo tiveram {} pessoas maiores de idade.'.format(maiores))
#print('Ao todo tiveram {} pessoas menores de idade.'.format(menores))





#maior=0
#menor=0
#for pessoa in range(1,6):
#    peso=float(input('Peso da {}°Pessoa:'.format(pessoa)))
#    if peso==1:
#        maior=peso
#        menor=peso
#    else:
#        if peso>menor:
#            maior=peso
#        if peso<menor:
#            menor=peso
#print("O maior peso lido foi o de {}Kg.".format(maior))
#print('O menor peso lido foi o de {}Kg.'.format(menor))






# from datetime import date
#atual=date.today().year
#maiores=0
#menores=0
#saldo=0
#for pessoa in range(1,8):
#    ano=int(input('A {}°Pessoa nasceu em: '.format(pessoa)))
#    saldo = atual - ano
#    if saldo>=18:
#        maiores = maiores+1
#    else:
#        menores = menores + 1
#print('\033[31mDentro da pesquisa existem {} pessoas maiores de idade.\033[m'.format(maiores))
#print('\033[33mDentro da pesquisa existem {} pessoas menores de idade.\033[m'.format(menores))




#n1=int(input('Digite o primeiro termo da P.A: '))
#r=int(input('Digite a razão da P.A: '))
#n10=n1+10*r
#print('Os elementos desta P.A são: ')
#for termos in range(n1,n10,r):
#    print('{}'.format(termos),end=',')


#soma=0
#for numeros in range(1,4):
#    soma=soma+numeros
#    print(numeros)
#print(soma)


maior=0
menor=0
for pessoa in range(1,5):
    peso=float(input('Peso da {}°Pessoa:'.format(pessoa)))
    if pessoa==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print("O maior peso lido foi o de {}Kg.".format(maior))
print('O menor peso lido foi o de {}Kg.'.format(menor))
































