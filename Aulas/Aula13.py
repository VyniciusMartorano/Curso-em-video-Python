'''cont=1
while cont<=10:
    print(cont,end='->')
    cont+=1
print('fim')'''


cont=s=0
while True:
    num=int(input('Digite um numero: '))
    if num==999:
        break
    s=s+num
print(f'A soma vale {s}')