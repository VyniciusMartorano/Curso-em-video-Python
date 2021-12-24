def fatorial(n=0,show=False):
    f=1
    print(f'O fatorial de {n} é: ')
    for c in range(n,0,-1):
        if show==True:
            print(c, end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f*=c
    return f




print(fatorial(5,True))





