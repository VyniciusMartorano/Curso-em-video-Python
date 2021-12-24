def ficha(jog = '<Desconhecido>',gol = 0):
    print(f'O jogador {jog} fez {gol} gols no campeonato.')


print('-'*35)
n=str(input('Nome: '))
g=str(input('gols: '))
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip()=='':
    ficha(gol=g)
else:
    ficha(n,g)
