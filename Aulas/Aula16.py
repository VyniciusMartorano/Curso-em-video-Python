'''pessoas=[]
vitor=['vitor',19]
maria=['maria',20]
pessoas.append(vitor[:])
pessoas.append(maria[:])
print(pessoas)
print(pessoas[1][1])        #Buscar o numero 20 na lista pessoas
'''

'''galera=[['joaquim',13],['joao',14],['ana',17],['maria',19]]
print(galera[2][0]) #Buscar ana
print(galera[1][1]) #Buscar a idade de joao
'''


'''galera=[['joaquim',13],['joao',14],['ana',17],['maria',19]]
for p in galera:
    print(f'{p[0]} Tem {p[1]} anos')'''


galera=[]
dado=[]
maior=menor=0
for c in range(0,3):
    dado.append(str(input('Digite o nome: ')).strip())
    dado.append(int(input('Digite a idade: ')))
    galera.append(dado[:])
    dado.clear()    #limpar dados
for p in galera:
    if p[1]>=18:
        print(f'{p[0]} é maior de idade.')
        maior+=1
    else:
        menor+=1
        print(f'{p[0]} é menor de idade.')
print(f'Temos um total de {maior} pessoas maiores de idade.')
print(f'Temos um total de {menor} pessoas menores de idade.')







