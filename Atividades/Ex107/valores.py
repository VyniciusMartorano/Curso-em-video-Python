def metade(p = 0, form=False):
    from Atividades.Ex107.moeda import moeda
    met = p / 2
    if form==True:
        return moeda(met,form)
    else:
        return met

def dobro(p = 0,form=False):
    from Atividades.Ex107.moeda import moeda
    dob = p * 2
    if form == True:
        return moeda(dob,form)
    else:
        return dob

def aumentar(p = 0, taxa = 0,form=False):
    from Atividades.Ex107.moeda import moeda
    mais=(p / 100) * taxa + p
    if form==True:
        return moeda(mais,form)
    else:
        return mais

def diminuir(p = 0, taxa = 0 ,form=False):
    from Atividades.Ex107.moeda import moeda
    menos= p - (p / 100) * taxa
    if form == True:
        return moeda(menos,form)
    else:
        return menos

