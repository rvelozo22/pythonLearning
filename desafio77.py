tupla = ('Macaco', 'Aviao', 'Caderno', 'Computador', 'Aviao',
         'Colirio', 'Creme', 'Pasta', 'Dado', 'Texto')

for i in tupla:

    print(f'A palavra {i.upper()} temos: ', end='')
    i = i.lower()
    for j in i:
        if j in 'aeiou':
            print(j, end = ' ')
    print('\n')
