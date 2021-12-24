def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO!Digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usuario não digitou um valor.\033[m')
        else:
            return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (TypeError, ValueError):
            print(f'\033[31mERRO!Digite um numero real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados foi interrompida pelo usuario.\033[m')
            return 0
        else:
            return float(num)


n = leiafloat('Digite um numero Real: ')
print(f'O numero digitado foi {n}')

num = leiaint('Digite um numero inteiro: ')
print(f'O numero digitado foi {num}')

