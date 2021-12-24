def ajuda():
    print('\033[42m~' * 35)
    print('     Sistema de ajuda PyHelp')
    print('~' * 35)
    com = str(input('\033[mFunção ou Biblioteca: '))
    while com != 'fim':
        print('\033[1;30;107m')
        help(com)
        print('\033[m\033[42m~'*35)
        print('     Sistema de ajuda PyHelp')
        print('~' * 35)
        com = str(input('\033[m     Função ou Biblioteca: '))
        print(f'Acessando a biblioteca {com}...')
    print('\033[1;45m~'*15)
    print('   Até logo!')
    print('~' * 15)




ajuda()