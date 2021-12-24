def voto(data):
    from datetime import date
    atual = date.today().year
    idade=atual-data
    if idade < 16:
        return f'Com {idade} anos: Você ainda não tem idade pra votar!'
    if idade >= 16 and idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'
    if idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'


#programa principal
print('-'*35)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
