x=float(input('Digite a distancia da viagem em KM: '))
c=x*0.50
l=x*0.45
if x<200:
    print('Sua viagem custara R${:.2f} ao todo.'.format(c))
else:
    print('Sua viagem custará R${:.2f} ao todo. '.format(l))
