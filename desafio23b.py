#Tratando como número

num = int(input('Digite um número de 0 a 9999:'))

milhar = num // 1000 % 10
centena = num // 100 % 10
dezena = num // 10 % 10
unidade = num // 1 % 10

print('\n')
print(f'Unidade: {unidade}\n')
print(f'Dezena: {dezena}\n')
print(f'Centena: {centena}\n')
print(f'Milhar: {milhar}')

