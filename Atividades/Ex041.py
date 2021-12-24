n1=float(input('\033[1mDigite a sua primeira nota:'))
n2=float(input("Digite sua segunda nota:\033[m"))
m=(n1+n2)/2
if m<5:
    print('\033[1;31mREPROVADO\033[m')
elif m>=5 and m<=6.9:
    print('\033[1;33mRECUPERAÇÃO\033[m')
else:
    print('\033[32mAPROVADO')