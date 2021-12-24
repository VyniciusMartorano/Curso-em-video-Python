n1=float(input('\033[1mDigite um numero:'))
n2=float(input('Digite outro numero:\033[m'))
if n1>n2:
    print('\033[31mO PRIMEIRO valor é MAIOR.')
elif n2>n1:
    print('O SEGUNDO valor é MAIOR')
else:
    print('Os DOIS valores sao IGUAIS.')

