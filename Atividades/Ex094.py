dados=dict()
gols=list()
dados['nome']=str(input('Nome: '))
tot=int(input(f'Quantas partidas {dados["nome"]} disputou? '))

for p in range(1,tot+1):
    gols.append(int(input(f'  Quantos gols na partida {p}?')))
dados['gols']=gols[:]
dados['total'] = sum(gols)          #sum() sever pra somar elementos de um conjunto

for k,v in dados.items():
    print(f'O campo {k} tem valor {v}')
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')

for k,v in enumerate(dados['gols']):
    print(f'   --->Na partida {k+1},fez {v} gols')
print(f'  Foi um total de {sum(dados["gols"])} gols')