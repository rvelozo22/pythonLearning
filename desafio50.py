soma = 0
lista = []

print('='*85)
print('Este programa somará os números pares que você digitar. Digite 6 números inteiros')
print('='*85)
print('\n')

for i in range(1,7):
    n = int(input(f'Número {i}: '))
    if n % 2 == 0:
        soma += n
        lista.append(n)

print('='*45)
print(f'Os valores somados são: {lista}')
print(f'O resultado é: {soma}')
print('='*45)
