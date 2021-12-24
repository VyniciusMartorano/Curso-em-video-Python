from datetime import date
ano=int(input("Que ano quer analisar? "))
x=ano%4
if x==0 and ano%100 !=0 or ano%400==0:
    print('{} é um ano BISSEXTO'.format(ano))
else:
    print('{} NÃO é um ano BISSEXTO.'.format(ano))
