distancia = float(input('Quantos kilometros foram rodados com o carro?'))
tempo = int(input('Quantos dias você ficou com o carro?'))
preço = (tempo*60)+(0.15*distancia)
print('O total a pagar é de R${:.2f}.'.format(preço))
