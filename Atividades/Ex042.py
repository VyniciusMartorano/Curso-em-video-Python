from datetime import date

atual= date.today().year
ano = int(input('Digite o ano que você nasceu para saber se ja esta na hora de se alistar:'))
sexo = str(input('Você é do sexo feminino ou masculino?')).strip().lower()
x = atual - ano
if sexo == 'masculino':
    if x>18:
        print('\033[1;31mVocê deveria ter se alistado à {} ano(s) atras!\033[m'.format(x-18))
    elif x<18:
        print('Você deverá se alistar ao serviço em até {} ano(s).'.format(18-x))
    elif x==18:
        print('Aliste-se imediatamente!')
elif sexo =='feminino':
    print('Mulheres não precisam se alistar!')
