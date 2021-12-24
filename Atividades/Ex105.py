def notas(*n,sit=False):
    soma = 0
    alunos={}
    notas=[]
    notas.append(n)
    alunos['Total'] = len(notas[0])
    alunos['Maior']=max(notas[0])
    alunos['Menor']=min(notas[0])
    for c in notas[0]:
        soma+=c
        alunos['Média']=(soma / len(notas[0]))
    if sit == True:
        if alunos['Média'] >= 7:
            alunos['Situação'] = 'BOA'
        if alunos['Média'] < 7:
            alunos['Situação']= 'RUIM'
        alunos['Média']=f'{alunos["Média"]:.2f}'
    print(alunos)


#Programa principal
notas(4,6,4,8,sit=True)