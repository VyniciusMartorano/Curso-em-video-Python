lista=[]
dado=[]
maior=menor=cont=mais=menos=0
while True:
    continuar=' '
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    lista.append(dado[:])
    dado.clear()
    cont+=1
    for p in lista:
        if cont==1:
            maior=p[1]
            menor=p[1]
        else:
            if p[1]>maior:
                maior=p[1]
                mais=p[0]
            if p[1]<menor:
                menor=p[1]
                menos=p[0]
    while continuar not in 'SN':
        continuar=str(input('Quer continuar? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Você cadastrou um total de {len(lista)} pessoas')
print(f'O maior peso foi {maior}Kg de {mais} ')
print(f'O menor peso foi {menor}Kg de {menos}')