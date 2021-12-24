print('\033[1;31m-='*10,'Indice de Massa Corporal/','-='*9)
peso=float(input('Digite o seu peso: '))
altura=float(input('Digite sua altura:' ))
imc=peso/(altura**2)
print('RESULTADO:\033[m')
if imc<18.5:
    print('\033[1;33mVocê esta abaixo do peso!\033[m')
elif imc>=18.5 and imc<25:
    print('\033[1;32mPESO IDEAL!')
elif imc>=25 and imc<30:
    print('SOBREPESO![m')
elif imc>=30 and imc<40:
    print('\033[1;31mOBESIDADE!')
elif imc>=40:
    print('OBESIDADE MÓRBIDA!')
print('\033[1;31m-='*10,'-='*22)