                                                #TUPLAS

#lanche=('hamburguer','suco','pizza','pudim')  #variavel composta
#print(lanche)

'''
lanche='hamburguer'
lanche='suco'
print(lanche)'''

''' 
lanche=('hamburguer','suco','pizza','pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
'''

'''
lanche=('hamburguer','suco','pizza','pudim','batata frita')
for cont in range(0,len(lanche)):
    print(lanche[cont])
    cont+=1
print(f'Voce tem {cont} opções no cardapio')
print('Comi pra caramba!')'''

#pos =posição do objeto
'''
lanche=('hamburguer','suco','pizza','pudim')
for pos,comida in enumerate(lanche):     
    print(pos)
    print(comida)'''



'''
a=(1,2,3,4)
b=(2,4,8)
c=b+a
print(c)
print(len(c))
print(c.count(2)) #contar quantas vezes tem o numero 2 em 'c'
print(c.index(3))  #pegar a primeira ocorrencia de 3
print(c.index(2)) #pegar a primeira ocorrencia de 2
print(c.index(2,1)) #pegar a posiçao do numero 2 na segunda ocorrencia'0,1
'''

'''
pessoa=('vitor','18','m','65.8')
print(pessoa)
del(pessoa)  #deletar a tupla.
'''


from random import randint
x=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os valores sorteados são: ')
print(' ')
for n in x:
    print(n,end=' ')
print(' ')
print(f'O valor minimo é {min(x)}')
print(f'O valor maximo é {max(x)}')







