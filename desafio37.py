num = int(input('Digite um número na base decimal: '))
print('\n Conversão de base')
print('-'*50)
base = int(input('Hexadecimal - 1\n\nOctal - 2\n\nBinário - 3\n\nSelecione para qual base deseja converter o número: '))
print('-'*50)

if base == 1:
    print(f'\nResultado = {hex(num)}')
elif base == 2:
    print(f'\nResultado = {oct(num)}')
elif base == 3:
    print(f'\nResultado = {bin(num)}')
else:
    print('\n Opção inválida!')
