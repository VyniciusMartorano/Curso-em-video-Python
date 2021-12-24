from Atividades.Ex107.valores import dobro,diminuir,aumentar,metade
from Atividades.Ex107.moeda import moeda

p = float(input('Digite o preço:R$'))
print(f'A metade de {moeda(p,True)} é {metade(p,True)}.')
print(f'O dobro de {moeda(p,True)} é {dobro(p,True)}.')
print(f'Aumentando 10%, temos {aumentar(p,10,True)}.')
print(f'Diminuindo em 13%, temos {diminuir(p,13,True)}.')

