continuar=''
media=menor=maior=contador=0
while continuar in 'S':
    num=int(input('\033[33mDigite um numero:'))
    continuar=str(input('Quer continuar?[S/N]')).strip().upper()
    contador+=1
    media=media+num
    if contador==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num
if continuar=='N':
    print(f'\033[32mVocê digitou {contador} numeros e a media foi {media/contador} \nO maior valor foi {maior} e o menor foi {menor}')



