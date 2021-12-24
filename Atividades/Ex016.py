prod=float(input("Qual o valor do produto em analise?R$"))
print('-------------------------------------------------------')
desc=(prod/100)*15
jur=(prod/100)*10
print('Pagando a vista você tem um desconto de R${:.2f} no produto.'.format(desc))
print('-------------------------------------------------------')
print('Pagando parcelado em até 12x no cartão, tem um acrescimo\n de R${:.2f} no valor total.'.format(jur))
print('-------------------------------------------------------')
