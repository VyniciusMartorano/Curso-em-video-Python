lista=[]
while True:
    continuar = x = ''
    lista.append(int(input('Digite um numero: ')))
    if 5 not in lista:
        x='Não Está'
    if 5 in lista:
        x='Está'
    continuar = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar=str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if continuar=='N':
        break
lista.sort(reverse=True)
print(' ')
print(f'Os valores em ordem decrescente são:\n {lista}')
print(' ')
print(f'Você Digitou {len(lista)} numeros')
print(f'O numero 5 {x} na lista.')