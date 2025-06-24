name = input('Digite seu nome completo: ')

upper = name.upper()
lower = name.lower()

letter = len(name.replace(' ', ''))

firstWord = len(name.split()[0])

print('\n')
print('='*70)
print(f'\nNome em letras maiúsculas: {upper}')
print(f'\nNome em letras minúsculas: {lower}')
print(f'\nEste nome tem {letter} letras!')
print(f'\nO primeiro nome tem {firstWord} letras!\n')
print('='*70)