from Ex115.lib.interface import leiaInt,cabeçalho


def arquivoExiste(nome):
    try:
        open(nome,'rt')
    except (FileNotFoundError):
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um ERRO ao criar o arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def LerArquivo(nome):
    try:
        a = open(nome,'rt')   #rt== ler arquivo de texto
    except:
        print('Houve um erro ao Ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(F'{"NOME":>5}{"IDADE":>31}')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} Anos')
    finally:
        a.close()


def cadastrar(arq,nome='Desconhecido',idade=0):
    try:
        a = open(arq,'at')   #at== append dentro do arquivo de texto
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados!')
        else:
            print(f'Novo registro de {nome} Adicionado')
            a.close()










