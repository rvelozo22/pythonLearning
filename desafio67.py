while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n <= 0:
        break
    print(f'\nA tabuada de {n} é: ')
    print('='*20)
    for i in range (1,11):
        print(f'{n} x {i} = {n*i}')
    print('='*20)
    print('\n')
print('\nPrograma finalizado!')