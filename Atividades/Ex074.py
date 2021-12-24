print('Data=24/07/2021')
times=('Palmeiras','Atletico-MG','Fortaleza','Bragantino','Athletico-PR',
       'Flamengo','Ceará SC','Fluminense','Bahia','Santos','Atlético-GO',
       'Corinthians','Internacional','Juventude','Cuiaba','São Paulo',
       'Sport Recife','America-MG','Grêmio','Chapecoense')
print(f'\033[32mOs times que disputam o campeonato são:\033[m\n\033[36m{times}\033[m')
print(' ')
print('Os 5 primeiros colocados são: ')
x=0
for cont in range(0,5):
       x=x+1
       print(x,'°',times[cont])
y=0
print(' ')
print('\033[31mOs 4 Ultimos colocados são:')
for c in range(15,20):
       y+=1
       print(y,'°',times[c])


print('\033[m ')
print(f'\033[1;32mTimes em ordem alfabetica:\033[m \033[36m\n{sorted(times)}')
print(' ')
pos=times.index('Chapecoense')
print(f'A Chapecoense esta na {pos}° Posição.')