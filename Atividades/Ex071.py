print('        BANCO CEV')
cinquenta=vinte=dez=um=resto=saida=0
print(' ')
valor=int(input('Qual o valor a ser sacado? R$'))
while True:
    print(' ')
    print('Serão sacadas as seguintes cédulas:')
    print(' ')
    if valor//50>=1:
        resto=valor%50
        cinquenta=valor//50
        print(f'Total de {cinquenta} Cédulas de cinquenta.')
    if resto>=20:
        vinte=resto//20
        resto=resto%20

        print(f'Total de {vinte} Cédulas de vinte.')
    if resto>=10:
        dez=resto//10
        resto=resto%10
        print(f'Total de {dez} Cédulas de R$10.')
    if resto>=1:
        um=resto//1
        print(f'Total de {um} cédulas de de R$1.')
    break
