print('\033[31m-='*20)
print("FORMADOR DE TRIANGULOS")
print("-="*20)
c1=float(input('Digite um segmento: '))
c2=float(input('Digite outro segmento: '))
c3=float(input('Digite outro segmento: '))
if c1+c2>c3 and c1+c3>c2 and c2+c3>c1:
    print("\033[34mOs segmentos acima PODEM formar um triangulo ",end='')
    if c1==c2==c3:
        print('EQUILATERO.')
    if c1 != c2 != c3 != c1:
        print('ESCALENO.')
    else:
        print('ISÓCELES.')
else:
    print('\033[34mOs segmentos acima NÃO PODEM formar um triangulo.')
    