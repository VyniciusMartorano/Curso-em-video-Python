import datetime
dados={}
dados['nome']=str(input('Nome: ')).strip()
dados['ano']=int(input('Ano de nascimento: '))
dados['ctps']=int(input('Carteira de trabalho(0 não tem): '))
dados['idade']=(datetime.date.today().year)-dados['ano']
if dados['ctps']==0:
    for k,v in dados.items():
        print(f'{k} tem valor: {v}')
if dados['ctps']!=0:
    dados['contratação']=int(input('Ano de contratação: '))
    dados['salario']=float(input('Salario: '))
    dados['aposentadoria']=dados['contratação']-dados['ano']+35
    for k,v in dados.items():
        print(f'{k} tem valor {v}')




