#nome=str(input('Qual o seu nome?'))
#if nome=='vitor':
#    print("\033[34mSeu nome é muito lindo.")
#elif nome=='maria' or nome=='pedro' or nome=='cleiton':
#    print('Seu nome é bem popular no Brasil!')
#elif nome in 'ana juliana jessica isabelle':
#    print("\033[35mBelo nome feminino!\033[m")
#else:
#    print("Seu nome é bem normalzinho")
#print('Tenha um bom dia {}'.format(nome))



#print('\033[31m-=\033[m'*6,'\033[1mEMPRESTIMOS PARA FINANCIAMENTO','\033[31m-=\033[m'*6)
#casa=float(input('\033[4mQual o valor da casa?R$'))
#salario=float(input('Qual o seu salario?R$'))
#tempo=int(input('Em quantos anos você quer pagar\033[m?'))
#print('\033[1;31m-=\033[m'*28)
#x=casa/(tempo*12)
#y=(salario/100)*30
#if x<y:
#    print('\033[32mParabens seu empréstimo foi APROVADO!')
#else:
#    print('\033[31mSeu emprestimo foi NEGADO.')



#n1=float(input('\033[1mDigite um numero:'))
#n2=float(input('Digite outro numero:\033[m'))
#if n1>n2:
#    print('\033[31mO PRIMEIRO valor é MAIOR.')
#elif n2>n1:
#    print('O SEGUNDO valor é MAIOR')
#else:
#    print('Os DOIS valores sao IGUAIS.')


#n1=float(input('\033[1mDigite a sua primeira nota:'))
#n2=float(input("Digite sua segunda nota:\033[m"))
#m=(n1+n2)/2
#if m<5:
#    print('\033[1;31mREPROVADO\033[m')
#elif m>=5 and m<=6.9:
#    print('\033[1;33mRECUPERAÇÃO\033[m')
#else:
#    print('\033[32mAPROVADO')



#print('#' * 100)
#print(' ' * 10, 'Digite o ano em que você nasceu para saber se esta na hora de se alistar!')
#print('#' * 100)
#from datetime import date
#atual = date.today().year
#sexo = str(input('Mas antes, você é de sexo masculino ou feminino? ')).strip().lower()
#if sexo == 'masculino':
#    print('Ok começaremos o processo...')
#    nasc = int(input('Ano de nascimento? '))
#    idade = atual - nasc
#    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
#    if idade == 18:
#        print('Você tem que se alistar IMEDIATAMENTE!')
#    elif idade < 18:
#        saldo = 18 - idade
#        print('Ainda faltam {} anos para o alistamento!'.format(saldo))
#        ano = atual + saldo
#        print('Seu alistamento será em {}'.format(ano))
#    elif idade > 18:
#        saldo = idade - 18
#        print('Você já deveria ter se alistado há {} anos!'.format(saldo))
#        ano = atual - saldo
#        print('Seu alistamento foi em {}'.format(ano))
#elif sexo == 'feminino':
#    print('Mulheres não precisam passar por o processo de alistamento!')
#else:
#    print('Por favor digite apenas "masculino" ou "feminino"')
#print('#' * 100)
#print(' ' * 44, 'Finish!')
#print('#' * 100)





















#from datetime import date

#atual= date.today().year
#ano = int(input('Digite o ano que você nasceu para saber se ja esta na hora de se alistar:'))
#sexo = str(input('Você é do sexo feminino ou masculino?')).strip().lower()
#x = atual - ano
#if sexo == 'masculino':
#    if x>18:
#        print('Você ja passou do tempo de se alistar!')
#    elif x<18:
#        print('Você fulturamente deverá se alistar ao serviço!')
#    elif x==18:
#        print('Chegou sua hora de se alistar!')
#elif sexo =='feminino':
#    print('Mulheres não precisam se alistar!')




from datetime import date
atual=date.today().year
print('\033[1;34m-=\033[m'*7,'CONFEDERAÇÃO NACIONAL DE NATAÇÃO','\033[1;34m-=\033[m'*7)
ano=int(input('Digite seu ano de nascimento:'))
idade= atual - ano
print('ATÉ 9 ANOS: \033[1;33mMIRIM\033[m\nATÉ 14 ANOS: \033[1;34mINFANTIL\033[m\nATÉ 19 ANOS: \033[1;32mJUNIOR\033[m\nATÉ 20 ANOS \033[1;31mSÊNIOR\033[m\nMAIS QUE 20 ANOS: \033[1;35mMASTER\033[m')
if idade<=20 and idade>19:
    print('Você esta incluso na categoria \033[1;31mSêNIOR\033[m')
elif idade>14 and idade<=19:
        print('Você esta incluso na categoria \033[1;32mJUNIOR\033[m')
elif idade>9 and idade<=14:
            print('Você esta incluso na categoria \033[1;34mINFANTIL\033[m')
elif idade<=9 and idade>0:
    print('Você esta incluso na categoria \033[1;33mMIRIM\033[m')
else:
    print('Você esta incluso na categoria \033[1;35mMASTER\033[m')
print('\033[1;34m-='*75)




















































































