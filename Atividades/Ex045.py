print('\033[1;34m''='*15,'LOJAS GUANABARA','='*15)
preço=float(input('Digite o valor das compras:R$'))
forma=int(input('FORMAS DE PAGAMENTO:\n\033[1;32m[ 1 ] À VISTA (DINHEIRO/CHEQUE)\n[ 2 ] À VISTA NO CARTÃO\n[ 3 ] EM ATÉ 2X NO CARTÃO\n[ 4 ] 3X OU MAIS NO CARTÃO(valor minimo:100R$)\033[m\nQual é a opção?\033[m'))
juros=(preço/100)*20+preço
if forma==1:
    print('\033[1;33mVocê escolheu o método à vista e recebeu 10% de desconto, total=R${:.2f}'.format(preço-(preço/100)*10))
elif forma==2:
    print('\033[33mVocê escolheu o método à vista no cartão e\n recebeu 5% de desconto,totalR${:.2f}.'.format(preço-(preço/100)*5))
elif forma==3:
    print('\033[33mSua compra será parcelada em 2x de {:.2f} no cartão \nque no final irá lhe custar um total de:R${:.2f}'.format(preço/2,preço))
elif forma==4 and preço>=100:
    x=int(input('\033[1;33mVocê deseja pagar em quantas vezes?'))
    if x<3:
        print('\033[1;33mO numero minimo de parcelas para esta opção é de 3x,Tente novamente!')
    if x >= 3:
        print('\033[4;36mSua compra será parcelada em {}x de R${:.2f} COM JUROS\nSUA COMPRA DE R${:.2f} vai custar R${:.2f} no final.\033[m'.format(x, (juros / x), preço, juros))
elif preço<100:
    print('O Valor minimo para esta forma de pagamento é de 100$, Tente novamente.')
print('\033[1;34m='*50)





















