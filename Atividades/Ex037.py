s=float(input('\033[36mQual o seu salario?R$'))
if s>1250.00:
    print("\033[34mVocê recebeu um aumento de 10%, e ago-\nra seu salário passará a ser R${:.2f}.".format((s/100)*10+s))
else:
    print('\033[34mVocê receberá um aumento de 15%, e ago-\nra seu salário passará a ser R${:.2f}.'.format((s/100)*15+s))
