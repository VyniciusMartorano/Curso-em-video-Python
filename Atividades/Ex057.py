sexo=''
while sexo!='M' and sexo!='F':
    sexo=str(input('[ M ]====Masculino\n[ F ]====Feminino\nQual o seu sexo?')).strip().upper()
    if sexo!='M' and sexo!='F':
        print('\033[31mOPÇÃO INVALIDA!\033[m')
if sexo=='F':
    print('\033[1;35mVocê é do sexo feminino.')
elif sexo=='M':
    print('\033[1;31mVocê é do sexo masculino.')

print('FIM!')

