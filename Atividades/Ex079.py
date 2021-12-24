lista=[]
maior=menor=mp=men=0
print('-'*50)
print('-'*50)
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-'*50)
print(f'Você Digitou os valores {lista}')
for p, v in enumerate(lista):
    print(f'O valor {v} foi encontrado na posição {p}')
    if p==0:
        maior=v
        menor=v
    else:
        if v>maior:
            maior=v
            mp=p
        if v<menor:
            menor=v
            men=p
print('-'*50)
print(f'O maior valor da lista é {max(lista)}, na posição {mp}')
print('-'*50)
print(f'O menor valor da lista é {min(lista)}, na posição {men}')









