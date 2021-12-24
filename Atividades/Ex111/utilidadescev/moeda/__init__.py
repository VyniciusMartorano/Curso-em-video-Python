def resumo(p,desc,aum):
    from Atividades.Ex107.valores import aumentar, diminuir, dobro, metade
    from Atividades.Ex107.moeda import moeda
    print('='*35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('='*35)
    print(f'{"Preço analisado:":<25}{moeda(p,True):>2}')
    print(f'{"Dobro do preço:":<25}{dobro(p,True):>2}')
    print(f'{"Metade do preço:":<25}{metade(p,True):>2}')
    print(f'{desc}{"% de redução:":<23}{diminuir(p,desc,True):>2}')
    print(f'{aum}{"% de aumento:":<23}{aumentar(p,aum,True):>2}')
    print('=' * 35)
