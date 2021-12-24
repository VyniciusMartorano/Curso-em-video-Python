
lista=[]
for posição in range(0,5):
    num=int(input('Digite um valor: '))
    if posição==0 or num > lista[-1]:
        lista.append(num)
        print('Seu numero foi adicionado ao final da lista.')
    else:
        pos=0
        while pos<len(lista):
            if num <= lista[pos]:
                lista.insert(pos,num)
                print(f'Seu numero foi adicionado a posição {pos}')
                break
            pos+=1
print(f'Os valores digitados em ordem crescente são {lista}')
