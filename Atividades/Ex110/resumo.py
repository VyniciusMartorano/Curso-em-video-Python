
def resumo(p=0,desc=0,aum=0):
    from Atividades.Ex107.valores import aumentar, diminuir, dobro, metade
    from Atividades.Ex107.moeda import moeda
    print('='*35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('='*35)
    print(f'{"Preço analisado:":<25}{moeda(p,True)}')
    print(f'{"Dobro do preço:":<25}{dobro(p,True)}')
    print(f'{"Metade do preço:":<25}{metade(p,True)}')
    print(f'{desc}{"% de redução:":<24}{diminuir(p,desc,True)}')
    print(f'{aum}{"% de aumento:":<24}{aumentar(p,aum,True)}')
    print('=' * 35)




