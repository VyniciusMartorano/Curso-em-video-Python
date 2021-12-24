v=float(input('Digite a velocidade que o seu carro passou no sinal: '))
if v>80:
    print('Voce foi multado em R${} por estar a {}Kms acima da velocidade permitida'.format((v-80)*7,v-80))
else:
    print('Parabéns você passou dentro do limite de velocidade!')
print('Limite permitido: 80km/h')
