#Tratando como string

str = str(input('Digite um número de 0 a 9999: '))
print ('\n')

if len(str) >= 5:
    print('Número inválido')
elif len(str) == 4:
    print(f'Milhar: {str[3]}\n')
    print(f'Centena: {str[2]}\n')
    print(f'Dezena: {str[1]}\n')
    print(f'Unidade: {str[0]}\n')
elif len(str) == 3:
    print(f'Milhar: 0\n')
    print(f'Centena: {str[2]}\n')
    print(f'Dezena: {str[1]}\n')
    print(f'Unidade: {str[0]}\n')
elif len(str) == 2:
    print(f'Milhar: 0\n')
    print(f'Centena: 0\n')
    print(f'Dezena: {str[1]}\n')
    print(f'Unidade: {str[0]}\n')
elif len(str) == 1:
    print(f'Milhar: 0\n')
    print(f'Centena: 0\n')
    print(f'Dezena: 0\n')
    print(f'Unidade: {str[0]}\n')






