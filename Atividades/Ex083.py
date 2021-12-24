from time import sleep
lista=[]
impar=[]
par=[]
while True:
    continuar=' '
    n=int(input('Digite um valor: '))
    while continuar not in 'SN':
        continuar=str(input('Quer continuar?[S/N] ')).upper()[0].strip()
    lista.append(n)
    lista.sort()
    if n % 2==0:
        par.append(n)
    else:
        impar.append(n)
    par.sort()
    impar.sort()
    if continuar == 'N':
        print('Fechando o programa...')
        sleep(2)
        print('Fim de programa!')
        break
print(f'Os numeros digitados foram:\n {lista}')
print(' ')
print(f'Os numeros impares Digitados são:\n {impar}')
print(' ')
print(f'Os numeres pares Digitados são:\n {par}')