time=[]
jogador={}
gols=[]

while True:
    gols.clear()
    jogador.clear()
    jogador['nome']=str(input('Nome: ')).strip().upper()
    jogador['partidas']=int(input(f'Quantas partidas {jogador["nome"]} Jogou? '))
    for p in range(1,jogador['partidas']+1):
        gols.append(int(input(f'Quantos gols na partida {p}? ')))

    jogador['gols']=gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())


    continuar=str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    while continuar not in 'SN':
        print('ERRO!Digite S ou N.')
        continuar=str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break


print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'*60)
for k,v in enumerate(time):
    print(f'{k:3} ',end='')
    for d in v.values():
        print(f'{str(d):<15} ',end='')
    print()
print('-='*30)


while True:
    busca=int(input('Mostrar dados de qual jogador?(999 = parar)'))
    if busca == 999:
        print('FIM DE PROGRAMA')
        break
    if busca > len(time):
        print(f'ERRO!Digite um numero entre 0 e {len(time)}.')
        busca = int(input('Mostrar dados de qual jogador?(999 = parar)'))
    else:
        print(f'---LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}---')
        for i,g in enumerate(time[busca]['gols']):
            print(f'Na partida {i+1} fez {g} gols.')










