a=int(input('Digite um valor: '))
b=int(input('Digite um valor: '))
c=int(input('Digite um valor: '))
d=int(input('Digite um valor: '))
tupla=(a,b,c,d)
print(' ')
print(tupla)
x=tupla.count(9)
if x>=1:
    print(f'O valor 9 apareceu {x}x.')
    print(' ')
y=tupla.count(3)
if y>=1:
    print(f'A primeira vez em que o valor 3 foi encontrado foi na {tupla.index(3)+1}° posição.')
print(' ')
print('Os numeros pares são:')
for cont in range(0,len(tupla)):
    num=tupla[cont]
    cont+=1
    if num%2==0:
        print(num,end=' ')
        print(sep=',')



