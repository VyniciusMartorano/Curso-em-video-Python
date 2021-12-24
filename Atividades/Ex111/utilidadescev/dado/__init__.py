def leiadin(x):
    valido = False
    while valido==False:
        entrada = str(input(x)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO!"{entrada}" não é um valor válido.')
        else:
            valido = True
            return float(entrada)


