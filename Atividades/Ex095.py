galera = list()
dados = dict()
soma=0
while True:
    dados.clear()
    dados['Nome']=str(input('Nome: '))
    dados['Sexo']=str(input('Sexo[M/F]: ')).strip().upper()
    while dados['Sexo'] not in 'MF':
        print('ERRO! por favor tente novamente.')
        dados['Sexo'] = str(input('Sexo[M/F]: ')).strip().upper()
    dados['Idade']=int(input('Idade: '))
    galera.append(dados.copy())
    soma+=dados['Idade']
    continuar=str(input('Quer continuar[S/N]? ')).strip().upper()[0]
    while continuar not in 'SN':
        print('ERRO!Responda apenas S OU N.')
        continuar = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'A média de idade das pessoas cadastradas é de {soma / len(galera):.2f} anos.')
print('As mulheres cadastradas foram:',end=' ')
for p in galera:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}',end=',')
print('As pessoas que estão acima da média são:',end=' ')
for p in galera:
    if p['Idade']>soma / len(galera):
        print(f'Nome: {p["Nome"]}-->Idade: {p["Idade"]}-->Sexo: {p["Sexo"]}',)