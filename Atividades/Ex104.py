def leiaint(n=(str(input('Digite um numero: ')))):
    while n.strip()=='':
        print('\033[31mERRO!Digite um numero inteiro válido.\033[m')
        n = (str(input('Digite um numero: ')))
    if n.isnumeric():
        num=int(n)
    else:
        while True:
            print('\033[31mERRO!Digite um numero inteiro válido.\033[m')
            n = (str(input('Digite um numero: ')))
            if n.isnumeric():
                break
        while n.strip() == '':
            print('\033[31mERRO!Digite um numero inteiro válido.\033[m')
            n = (str(input('Digite um numero: ')))
        if n.isnumeric():
            num = int(n)

    print(f'O numero digitado foi {num}.')


leiaint()