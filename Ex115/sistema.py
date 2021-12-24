from Ex115.lib.interface import *   #'*' importa tudo
from time import sleep
from Ex115.lib.Funcionamento import *
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criararquivo(arq)



while True:
    resposta= menu(['Ver Pessoas Cadastradas','Cadastrar Pessoas','Fechar programa'])


    if resposta == 1:
        sleep(1 / 2)
        LerArquivo(arq)
        print()
        print()
        print()



    elif resposta == 2:
        sleep(1 / 2)
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(1)





    elif resposta == 3:
        sleep(1 / 2)
        cabeçalho('Saindo do sistema... Até logo!')
        break




    else:
        sleep(1)
        print('\033[31mERRO! Digite uma opção válida!\033[m')