conteudo={}
conteudo['Nome']=str(input('nome: '))
conteudo['Média']=float(input(f'Media de {conteudo["Nome"]}: '))
if conteudo['Média']>=7:
    conteudo['situação']='Aprovado'
else:
    conteudo['situação']='Reprovado'
print(f'O nome é {conteudo["Nome"]}')
print(f'A média é igual a {conteudo["Média"]}')
print(f'Situação igual a {conteudo["situação"]}')
print(conteudo)



