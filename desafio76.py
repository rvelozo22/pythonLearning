tupla = ('Leite', 5.50, 'Pao', 6.60, 'Manteiga', 10, 'Atum', 9.9, 'Torrada', 4.5)

print('='*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('='*40)

for i in tupla:
    if isinstance(i,str):
        print(f'{i:.<30}', end='')
    # print(f'{'.':>35}', end='')
    if isinstance(i,int) or isinstance(i,float):
        print(f'R$', end='')
        print(f'{i:>7.2f}')
print('='*40)