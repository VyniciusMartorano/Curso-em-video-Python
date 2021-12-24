extnumeros=('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
         'Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Desoito','Desenove','Vinte')

while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if numero<0 or numero>20:
        print('Tente novamente!')
    if 0<=numero<=20:
        posição = extnumeros[numero]
        print(f'Você digitou o numero {posição}')
    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N]')).upper()[0].strip()
    if continuar == 'N':
        print("Fim de programa!")
        break