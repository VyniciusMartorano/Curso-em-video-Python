dados=[]
cache=[]
cont=0
fim=' '
print('-='*10,'\033[33mBOLETIM ESCOLAR\033[m','-='*10)
while True:
    while True:
        print('='*6,'CADASTRO DE ALUNO','='*6)
        nome=str(input(f'Nome: ')).strip().title()
        n1=float(input('1° nota: '))
        while n1<0 or n1>10:
            print('Nota INVALIDA!\nA nota deve estar no intervalo 0<=n<=10')
            n1 = float(input('1° nota: '))
        n2=float(input('2° nota: '))
        while n2<0 or n2>10:
            print('Nota INVALIDA!\nA nota deve estar no intervalo 0<=n<=10')
            n2 = float(input('2° nota: '))
        cont += 1
        media=(n1+n2)/2
        cache.append(nome)
        cache.append(n1)
        cache.append(n2)
        cache.append(media)
        dados.append(cache[:])
        dados.sort()
        print(dados)
        cache.clear()
        continuar = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
        while continuar not in 'SN':
            continuar = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
        if continuar == 'N':
            break
    print('SELECIONE UMA OPÇÃO:')
    print('[ 1 ] VER TODAS AS NOTAS\n'
          '[ 2 ] SELECIONAR UM ALUNO')
    selecione=int(input('Qual a sua escolha?'))
    while selecione!=1 and selecione!=2:
        print('OPÇÃO INVALIDA!')
        selecione = int(input('Qual a sua escolha?'))
    print('-='*30)
    if selecione == 1:
        for c in range(0,cont):
            print(f'NOME: {dados[c-1][0]}\nNOTA 1: {dados[c-1][1]:.2f}'
                  f'\nNOTA 2: {dados[c-1][2]:.2f}\nMÉDIA: {dados[c-1][3]:.2f}')
            print('-='*30)
    if selecione == 2:
        for c in range(0,cont):
            print(f'[ {c} ] {dados[c-1][0]}')
        escolha=int(input('Qual opção? '))
        while escolha <0 or escolha>cont-1:
            escolha = int(input('Qual opção? '))
        print(f'Voce escolheu a opção {escolha}')
        print(f'Nome: {dados[escolha-1][0]}\n'
              f'NOTA 1: {dados[escolha-1][1]:.2f}\n'
              f'NOTA 2: {dados[escolha-1][2]:.2f}\n'
              f'MÉDIA: {dados[escolha-1][3]:.2f}')
    sair=str(input('Deseja sair?[S/N]')).strip().upper()[0]
    while sair not in 'SN':
        sair = str(input('Deseja sair?[S/N]')).strip().upper()[0]
    if sair == 'S':
        break

