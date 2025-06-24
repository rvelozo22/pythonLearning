name = str(input('Olá! Digite seu nome completo: '))

name = name.split()

size = len(name) - 1

print('\n')
print(f'Olá {name[0]}! Prazer em conhece-lo(a)!\n')
print(f'Seu primeiro nome é {name[0]} e seu último nome é {name[size]}')
