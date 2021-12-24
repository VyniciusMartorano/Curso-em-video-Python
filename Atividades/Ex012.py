L=float(input('Largura da parede em metros='))
C=float(input('Comprimento da parade em metros='))
A=C*L
T=2
print('A sua parede tem dimensão {} x {}'.format(L,C))
print('Area da parede em metros quadrados= {:.2f}'.format(A))
print('Seram precisos {:.2f}l de tinta para pintar essa parede'.format(A/T))

