def linha(tam=42):
    return '-'*tam

def cabeçalho(txt):
    print(linha())
    print(f'{txt:^42}')
    print(linha())

def leiaInt(n):
    while True:
        try:
            num = int(input(n))
        except:
            print('ERRO!Digite um numero inteiro válido')
            continue
        else:
            return num




def menu(lista):
    cabeçalho('Menu Principal')
    cont=1
    for item in lista:
        print(f'\033[33m{cont}\033[m-\033[34m{item}\033[m')
        cont+=1
    print(linha())
    opc = leiaInt('\033[33mSua Opção: \033[m')
    return opc








