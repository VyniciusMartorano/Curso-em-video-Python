maior=0
menor=0
for pessoa in range(1,5):
    peso=int(input('Peso da {}°pessoa: '.format(pessoa)))
    if pessoa==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print("O maior peso é {}KG e o menor é {}KG.".format(maior,menor))
