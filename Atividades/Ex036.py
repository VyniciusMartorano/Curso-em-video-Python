n=float(input('\033[33mDigite um numero: '))
n2=float(input("\033[33mDigite outro numero: "))
n3=float(input('\033[33mDigite outro numero: '))
if n>n2:
        if n > n3:
                print('\033[36m{:.2f} é o MAIOR numero'.format(n))
if n2>n:
        if n2>n3:
                print('\033[36m{:.2f} é o MAIOR numero'.format(n2))
if n3>n2:
        if n3>n:
                print('\033[36m{:.2f} é o MAIOR numero'.format(n3))

if n<n2:
        if n<n3:
                print("\033[36m{:.2f} é o MENOR numero".format(n))
if n2<n:
        if n2<n3:
                print("\033[36m{:.2f} é o MENOR numero".format(n2))
if n3<n:
        if n3<n2:
                print("\033[36m{:.2f} é o MENOR numero".format(n3))