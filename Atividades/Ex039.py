print('\033[31m-=\033[m'*6,'\033[1mEMPRESTIMOS PARA FINANCIAMENTO','\033[31m-=\033[m'*6)
casa = float(input('\033[4mQual o valor da casa?R$'))
salario = float(input('Qual o seu salario?R$'))
tempo = int(input('Em quantos anos você quer pagar\033[m?'))
print('\033[1;31m-=\033[m'*28)
x = casa/(tempo*12)
y = (salario/100)*30
if x < y:
    print('\033[32mParabens seu empréstimo foi APROVADO!')
else:
    print('\033[31mSeu emprestimo foi NEGADO.')