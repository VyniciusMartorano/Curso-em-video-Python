lista=[[[],[],[]],[[],[],[]],[[],[],[]]]
for n in range(0,3):
    num=int(input(f'Digite o valor para a posição {[0] ,[n]}:'))
    lista[0][n].append(num)
for n in range(0, 3):
    num=int(input(f'Digite o valor para a posição {[1] ,[n]}:'))
    lista[1][n].append(num)
for n in range(0,3):
    num=int(input(f'Digite o valor para a posição {[2] ,[n]:}'))
    lista[2][n].append(num)
print(f'{lista[0][0]}{lista[0][1]}{lista[0][2]}')
print(lista[1][0],lista[1][1],lista[1][2])
print(lista[2][0],lista[2][1],lista[2][2])

