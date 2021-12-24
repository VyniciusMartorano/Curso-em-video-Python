soma=preçobarato=caro=prodbarato=cont=cont2=0

while True:
    produto=str(input("Qual o nome do produto? ")).strip().title()
    preço=float(input('Qual o preço do produto? '))
    soma=soma+preço
    cont+=1
    if cont==1:
        caro=preço
        preçobarato=preço
    else:
        if preço>caro:
            caro=preço
        if preço<preçobarato:
            preçobarato=preço
            prodbarato=produto
    if preço>1000:
        cont2+=1

    continuar=' '
    while continuar not in 'SN':
        continuar=str(input('Quer continuar?[S/N]')).upper()[0].strip()
    if continuar=='N':
        break
print('  ')
print(f'O total gasto na compra foi de R${soma}.')
print(f'O produto mais barato foi o {produto} e ele custou R${preçobarato}.')
print(f'{cont2} produtos custaram mais que 1000R$.')
