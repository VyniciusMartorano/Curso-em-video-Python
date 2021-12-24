lista=[[],[]]
num=0
for n in range(1,8):
    num=int(input(f'Digite o {n}° valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
    lista[0].sort()
    lista[1].sort()
print('-='*35)
print(f'Os valores pares são:\n{lista[0]}')
print(f'Os valores impares são:\n{lista[1]}')
print('-='*35)
