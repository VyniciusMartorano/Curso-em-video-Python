contmulher=conthomem=contpessoa=0
continuar=' '
while True:
    idade=int(input('Qual a idade? '))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('Qual o sexo?[M/F] ')).strip().upper()[0]
    if sexo == 'F':
        if idade < 20:
            contmulher += 1
    if sexo == 'M':
        conthomem += 1
    if idade > 18:
        contpessoa += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if continuar=='N':
        print('=-=' * 7, 'FIM DO PROGRAMA', '=-=' * 7)
        break
    continuar=' '
print(f'Total de pessoas com mais de 18 anos: {contpessoa}')
print(f'Ao todo temos {conthomem} homems cadastrados.')
print(f'E temos {contmulher} mulher(es) com menos de 20 anos cadastrada(s)')






