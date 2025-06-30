import random

ranNum = random.randrange(0, 5)

num = int(input('Digite um número de 0 a 5 e vou te dizer se foi o mesmo que eu pensei: '))

print('\n')
print('='*45)
print(f'Na mosca! Pensamos no número {ranNum}!' if num == ranNum else f'Tente novamente, eu pensei no número {ranNum}')
print('='*45)
