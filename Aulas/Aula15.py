#num=[9,6,0,3]       #lista
#num[2]=9           #trocar o elemento na lista
#num.append(35)  #acrescentar um elemento na lista
#num.sort()        #ordernar a lista em ordem crescente
#print(num)
#print(f'Esta lista tem {len(num)} Elementos.')


#num=[9,4,7,2]
#num.sort(reverse=True)    #Ordenar a lista em ordem decrescente
#print(num)


#num=[5,7,2,9]
#num.insert(2,1)     #Colocar o numero 1 na posição 2, assim empurrando os seguintes pra frente.
#print(num)



#num=[8,5,9,3]
#num.pop()           #Eliminar o ultimo valor da lista, Se num.pop(2) iria eliminar o elemento da posição 2
#print(num)


#num=[0,2,9,2,5]
#num.remove(2)           #eliminar o valor que esta na posição 2
#print(num)



#lista=[]
#lista.append(2)
#lista.append(9)
#lista.append(3)
#print(lista)
#for p,v in enumerate(lista):
#    print(f'Encontrei o valor {v} na posição {p}')



#lista=[]
#for pos in range(0,5):
#    lista.append(int(input('Digite um valor: ')))
#for p, v in enumerate(lista):
#    print(f'Encontrei o valor {v} na posição {p}')



#a=[2,7,4,9]
#b=a[:]
#b[3]=4
#print(a)
#print(b)


#a=[1,2,3]
#b=[]
#b.append(a[:])     #colocar A dentro de B
#print(b)




pessoas=[]
vitor=['vitor',19]
maria=['maria',20]
pessoas.append(vitor[:])
pessoas.append(maria[:])
print(pessoas)
print(pessoas[1][1])        #Buscar o numero 20 na lista pessoas







