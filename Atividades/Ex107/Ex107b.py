from Atividades.Ex107.valores import dobro,metade,aumentar,diminuir
from Atividades.Ex107 import moeda
p = float(input('Digite o preço:R$'))
print(f'A metade de R${p} é {metade(p,True)}.')
print(f'O dobro de R${p} é {metade(p,True)}.')
print(f'Aumentando 10%, temos {aumentar(p,10,True)}.')
print(f'Diminuindo em 13%, temos {diminuir(p,13,True)}.')