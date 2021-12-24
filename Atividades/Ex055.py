import datetime

atual=datetime.date.today().year
testar=0
maiores=0
menores=0
for pessoa in range(1,8):
    ano = int(input('Em que ano a {}°pessoa nasceu? '.format(pessoa)))
    testar=atual-ano
    if testar>=21:
        maiores=maiores+1
    else:
        menores=menores+1
print('Ao todo tiveram {} pessoas maiores de idade.'.format(maiores))
print('Ao todo tiveram {} pessoas menores de idade.'.format(menores))


