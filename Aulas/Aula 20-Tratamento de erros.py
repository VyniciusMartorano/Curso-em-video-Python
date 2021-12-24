try:
    a = int(input('Primeiro valor: '))
    b = int(input('Segundo valor: '))
    div = a / b
except (ValueError, TypeError):
    print('Tivemos um erro com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print('O usuario nao digitou nenhum valor.')
else:
    print(f'O resultado de {a}/{b} é {div}')
finally:
    print('Volte sempre!')