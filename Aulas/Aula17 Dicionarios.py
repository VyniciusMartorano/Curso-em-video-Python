#DICIONARIO
#pessoas={'nome': 'Vitor','sexo':'M','idade':18}
#print(pessoas['idade'])             #buscar idade no dicionario


'''pessoas={'nome': 'Vitor','sexo':'M','idade':18}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())       #saida: 'nome','sexo','idade'
print(pessoas.values())     #saida: 'vitor','M','18'
for k in pessoas.keys():
    print(k)                #saida: 'nome','sexo','idade'
for v in pessoas.values():
    print(v)                #saida: 'vitor','M','18'
for v,k in pessoas.items():
    print(f'{k}={v}')
pessoas['nome']='leandro'  #trocar o valor de nome para 'leandro'
'''



'''brasil=[]
estado1={'UF':'Rio de janeiro','sigla':'RJ'}
estado2={'UF':'São paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(f'{brasil[0]["sigla"]}={brasil[0]["UF"]}')
'''

estado={}
brasil=[]
for c in range(0,2):
    estado['uf']=str(input('Unidade federativa:'))
    estado['sigla']=str(input('Sigla do estado:'))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in estado.items():
        print(f'o campo {k} tem valor {v}')











