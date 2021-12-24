import math
print('Medir hipotenusa do triangulo retangulo')
op=float(input('Digite o valor do cateto oposto em metros:'))
ad=float(input('Digite o valor do cateto adjacente em metros:'))
hip =math.sqrt((op**2)+(ad**2))
print('A hipotenusa mede {:.2f}m'.format(hip))

