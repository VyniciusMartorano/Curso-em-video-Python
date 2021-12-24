import time
time=time.localtime()
x='LIVE BIKE'
print('{:^35}'.format(x))
print('=-='*10)
nome=''
dados1=[]
dados2=[]
cache=[]
while True:
    marcha = preçoc = preços = semmarcha = total = 0
    print('\033[31m[1] Aluguel por hora\n'
          '[2] Aluguel por diária\n'
          '[3] Verificar dados cadastrais\n'
          '[4] Fechar programa\033[m')
    opção=int(input('Qual a sua opção?'))
    while opção !=1 and opção!=2 and opção!=3:
        print('Opção invalida!')
        opção = int(input('Qual a sua opção?'))
    #OPÇÃO MINIMIZADA
    if opção == 1:                                    #ALUGUEL PELA DIARIA
        nome=str(input('Nome do cliente:')).strip().title()
        cpf=int(input('CPF do cliente: '))
        quantidade=int(input('Quantas bikes são?'))
        for c in range(1,quantidade+1):
            tipo=int(input(f'[1] C/ MARCHA\n[2] S/ MARCHA\nQual o tipo da {c}° Bike? '))
            if tipo==1:
                preçoc=12
                marcha+=1
            if tipo==2:
                preços=10
                semmarcha+=1
        hora=int(input('Quantas horas de aluguel? '))
        total=(marcha*preçoc*hora)+(semmarcha*preços*hora)
        print(f'Total de R${total}.')
        forma = int(input('Forma de pagamento:\n[ 1 ] Cartão\n[ 2 ] Dinheiro\n[ 3 ] PIX\nQual a sua escolha? '))
        while forma != 1 and forma != 2 and forma != 3:
            forma = int(input('Forma de pagamento:\n[ 1 ] Cartão\n[ 2 ] Dinheiro\n[ 3 ] PIX\nQual a sua escolha? '))
        if forma == 1:
            forma = 'Cartão'
        if forma == 2:
            forma = 'Dinheiro'
        if forma == 3:
            forma = 'PIX'
        tempinicio=input('Horario de partida: ')
        tempchegada=input('Horario de chegada: ')
        cache.append(nome)  #0
        cache.append(cpf)   #1
        cache.append(marcha)    #2
        cache.append(semmarcha)     #3
        cache.append(tempinicio)    #4
        cache.append(tempchegada)   #5
        cache.append(total)         #6
        cache.append(forma)         #7
        print('Confirme seus dados:')
        print(f'nome: {nome}')
        print(f'Cpf: {cpf}')
        print(f'Bikes com marcha: {marcha}')
        print(f'Bikes sem marcha: {semmarcha}')
        print(f'Hora de inicio: {tempinicio}')
        print(f'Hora de chegada: {tempchegada}')
        print(f'Valor total: R${total}')
        print(f'Forma de pagamento: {forma}')
        confirmar=str(input('Você confirma que os dados estão corretos?[S/N]')).strip().upper()[0]
        while confirmar not in 'SN':
            print('Opção INVALIDA!')
            confirmar = str(input('Você confirma que os dados estão corretos?[S/N]')).strip().upper()[0]
        if confirmar== 'S':
            dados1.append(cache[:])
            cache.clear()
        while confirmar == 'N':
            cache.clear()
            nome = str(input('Nome do cliente:')).strip().title()
            cpf = int(input('CPF do cliente: '))
            quantidade = int(input('Quantas bikes são?'))
            for c in range(0, quantidade):
                tipo = int(input(f'[1] C/ MARCHA\n[2] S/ MARCHA\nQual a sua {c}° opção?'))
                if tipo == 1:
                    preçoc = 12
                    marcha += 1
                if tipo == 2:
                    preços = 10
                    semmarcha += 1
            hora = int(input('Quanto tempo de aluguel(Em Horas)? '))
            total = (marcha * preçoc * hora) + (semmarcha * preços * hora)
            print(f'Total de R${total}.')
            forma=int(input('Forma de pagamento:\n[ 1 ] Cartão\n[ 2 ] Dinheiro\n[ 3 ] PIX\nQual opção?'))
            while forma !=1 and forma != 2 and forma != 3:
                forma = int(input('Forma de pagamento:\n[ 1 ] Cartão\n[ 2 ] Dinheiro\n[ 3 ] PIX\nQual opção?'))
            tempinicio = input('Horario de partida: ')
            tempchegada = input('Horario de chegada: ')
            dados1.append(nome)  # 0
            dados1.append(cpf)  # 1
            dados1.append(marcha)  # 2
            dados1.append(semmarcha)  # 3
            dados1.append(tempinicio)  # 4
            dados1.append(tempchegada)  # 5
            dados1.append(total)  # 6
            dados1.append(forma)
            print('Confirme seus dados:')
            print(f'nome: {nome}')
            print(f'Cpf: {cpf}')
            print(f'Bikes com marcha: {marcha}')
            print(f'Bikes sem marcha: {semmarcha}')
            print(f'Hora de inicio: {tempinicio}')
            print(f'Hora de chegada: {tempchegada}')
            print(f'Valor total: R${total}')
            print(f'Forma de pagamento: {forma}')
            confirmar = str(input('Você confirma que os dados estão corretos?[S/N]')).strip().upper()[0]
            while confirmar not in 'SN':
                print('Opção INVALIDA!')
                confirmar = str(input('Você confirma que os dados estão corretos?[S/N]')).strip().upper()[0]
    if opção == 2:
        nome=str(input('Nome do cliente: ')).strip().title()
        cpf=int(input('CPF do cliente: '))
        endereço=str(input('Endereço: ')).strip().title()
        dia=int(input('Quantos dias de aluguel? '))
        quantidade = int(input('Quantas bikes são? '))
        for c in range(1, quantidade + 1):
            tipo = int(input(f'[1] C/ MARCHA\n[2] S/ MARCHA\nQual o tipo da {c}° Bike? '))
            if tipo == 1:
                preçoc = 60
                marcha += 1
            if tipo == 2:
                preços = 50
                semmarcha += 1
        total=(preçoc*marcha*dia)+(preços*semmarcha*dia)

        print(f'Total de R${total}.')

        forma = int(input('Forma de pagamento:\n[ 1 ] Cartão\n[ 2 ] Dinheiro\n[ 3 ] PIX\nQual a sua escolha? '))

        while forma != 1 and forma != 2 and forma != 3:
            forma = int(input('Forma de pagamento:\n[ 1 ] Cartão\n[ 2 ] Dinheiro\n[ 3 ] PIX\nQual a sua escolha? '))
        if forma == 1:
            forma = 'Cartão'
        if forma == 2:
            forma = 'Dinheiro'
        if forma == 3:
            forma = 'PIX'
        dataentrega=str(input('Data em que a bicicleta foi entregue: '))
        datarecebimento=str(input('Data de devolução: '))
        cache.append(nome)  #0
        cache.append(cpf)   #1
        cache.append(endereço)  #2
        cache.append(dia)      #3
        cache.append(marcha)    #4
        cache.append(semmarcha)    #5
        cache.append(total)         #6
        cache.append(forma)         #7
        cache.append(dataentrega)         #8
        cache.append(datarecebimento)         #9
        print(' ')
        print('CONFIRA SEUS DADOS:')
        print(' ')
        print(f'Nome: {nome}')
        print(f'CPF: {cpf}')
        print(f'Endereço: {endereço}')
        print(f'Tempo de uso: {dia} Dias')
        print(f'Bicicletas com marcha: {marcha}')
        print(f'Bicicletas sem marcha: {semmarcha}')
        print(f'Total: R${total}')
        print(f'Forma de pagamento: {forma}')
        print(f'Dia de entrega: {dataentrega}')
        print(f'Dia do recebimento: {datarecebimento}')
        print(' ')
        confirmar=str(input('Você :confirma que TODOS os dados'
                            ' acima estão corretos?[S/N]')).strip().upper()[0]
        while confirmar not in 'SN':
            confirmar = str(input('Você :confirma que TODOS os'
                                  ' dados acima estão corretos?[S/N]')).strip().upper()[0]
        if confirmar == 'S':
            dados2.append(cache[:])
            cache.clear()
        while confirmar =='N':
            nome = str(input('Nome do cliente: ')).strip().title()
            cpf = int(input('CPF do cliente: '))
            endereço = str(input('Endereço: ')).strip().title()
            dia = int(input('Quantos dias de aluguel? '))
            quantidade = int(input('Quantas bikes são? '))
            for c in range(1, quantidade + 1):
                tipo = int(input(f'[1] C/ MARCHA\n[2] S/ MARCHA\nQual o tipo da {c}° Bike? '))
                if tipo == 1:
                    preçoc = 60
                    marcha += 1
                if tipo == 2:
                    preços = 50
                    semmarcha += 1
            total = (preçoc * marcha * dia) + (preços * semmarcha * dia)

            print(f'Total de {total}.')

            forma = int(input('Forma de pagamento:\n[ 1 ] Cartão\n[ 2 ] Dinheiro\n[ 3 ] PIX\nQual a sua escolha? '))

            while forma != 1 and forma != 2 and forma != 3:
                forma = int(input('Forma de pagamento:\n[ 1 ] Cartão\n[ 2 ] Dinheiro\n[ 3 ] PIX\nQual a sua escolha? '))
            if forma == 1:
                forma = 'Cartão'
            if forma == 2:
                forma = 'Dinheiro'
            if forma == 3:
                forma = 'PIX'
            dataentrega = str(input('Data em que a bicicleta foi alugada: ')).strip()
            datarecebimento = str(input('Data de devolução: ')).strip()
            cache.append(nome)  # 0
            cache.append(cpf)  # 1
            cache.append(endereço)  # 2
            cache.append(dia)  # 3
            cache.append(marcha)  # 4
            cache.append(semmarcha)  # 5
            cache.append(total)  # 6
            cache.append(forma)  # 7
            cache.append(dataentrega)  # 8
            cache.append(datarecebimento)  # 9
            print(' ')
            print('CONFIRA SEUS DADOS:')
            print(' ')
            print(f'Nome: {nome}')
            print(f'CPF: {cpf}')
            print(f'Endereço: {endereço}')
            print(f'Tempo de uso: {dia} Dias')
            print(f'Bicicletas com marcha: {marcha}')
            print(f'Bicicletas sem marcha: {semmarcha}')
            print(f'Total: {total}')
            print(f'Forma de pagamento: {forma}')
            print(f'Dia de entrega: {dataentrega}')
            print(f'Dia do recebimento: {datarecebimento}')
            print(' ')
            confirmar = str(input('Você confirma que TODOS os dados'
                                  ' acima estão corretos?[S/N]')).strip().upper()[0]
            while confirmar not in 'SN':
                confirmar = str(input('Você confirma que TODOS os'
                                      ' dados acima estão corretos?[S/N]')).strip().upper()[0]
    if opção == 3:
        print(dados1)
    if opção == 4:
        fechar=str(input('Tem certeza de que deseja fechar o programa?[S/N]')).strip().upper()[0]
        while fechar not in 'SN':
            fechar = str(input('Tem certeza de que deseja fechar o programa?[S/N]')).strip().upper()[0]
        if fechar == 'S':
            break










