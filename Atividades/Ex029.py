x=str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(x.count('A')))
print('A letra A aparece pela primeira vez na {}° posição'.format(x.upper().find('A')))
print('A letra A aparece pela ultima vez na {}° posição.'.format(x.upper().rfind('A')))