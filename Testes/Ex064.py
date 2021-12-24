from math import log10
x=0
cont=0
soma=0
while x!= 999:
    x = int(input('Digite um valor \033[31m[999 para parar o programa]\033[m: '))
    cont+=1
    soma=soma+x
print(f'\033[32mVocê Digitou {cont-1} numeros e a soma deles é {soma-999}. ')


