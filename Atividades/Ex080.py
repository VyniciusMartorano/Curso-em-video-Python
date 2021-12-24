lista=[]
cont=0
while True:
    continuar=' '
    num=int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Valor duplicado! Não vou adicionar...')
    while continuar not in 'SN':
        continuar=str(input('Quer continuar?')).strip().upper()[0]
    if continuar=='N':
        print('=-'*30)
        print(f'Você digitou os valores:\n{sorted(lista)}')
        break

