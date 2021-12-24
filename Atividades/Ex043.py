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


