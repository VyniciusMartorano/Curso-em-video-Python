print('\033[33m=-='*7,'TABUADA','\033[33m=-=\033[m'*7)
cont=0
while True:
    cont = 0
    num=int(input('\033[33mQuer ver a tabuada de qual valor?\033[m'))
    if num<0:
        break
    print('=' * 28)
    for c in range(1,11):
        cont += 1
        print(f'\033[1;34m{cont} x {num} = {cont*num}')
    print('=' * 28)
print('\033[34mPROGRAMA TABUADA ENCERRADO. Volte sempre!')