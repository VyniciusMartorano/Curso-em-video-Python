cont=soma=0
while True:
    num=int(input('Digite um valor(\033[31m999 para parar\033[m): '))
    if num == 999:
        break
    soma+=num
    cont+=1
print(f'Você digitou {cont} numeros e a soma deles é {soma}')
