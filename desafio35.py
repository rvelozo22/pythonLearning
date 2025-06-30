print('Este programa realizará o check da desigualdade triângular!')
print('A soma de 2 lados deve ser maior que o 3º lado.')
print('-'*15)
print('a+b > c')
print('a+c > b')
print('b+c > a')
print('-'*15)
print('\n')

a = float(input('Reta a: '))
b = float(input('Reta b: '))
c = float(input('Reta c: '))

cond1 = a+b
cond2 = a+c
cond3 = b+c

if cond1 > c and cond2 > b and cond3 > a:
    print('As retas inseridas podem compor um triângulo!')
else:
    print('Os valores inseridos não são válidos para compor um triângulo')
