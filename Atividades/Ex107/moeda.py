def moeda(valor = 0, form=False):
    formatado = f'R${valor:.2f}'.replace('.', ',')
    if form == True:
        return formatado
    else:
        return valor
