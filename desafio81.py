lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    if str(input('Deseja digitar mais um valor? [S/N]')).strip().upper() == 'N':
        break

print(f'Foram digitados {len(lista)} valores!')
lista.sort(reverse=True)
print(f'Lista dos valores digitados em ordem decrescente: {lista}')

if 5 in lista:
    print('O número 5 está presente na lista, na(s) posição(oes): ', end='')
    for i, v in enumerate(lista):
        if v == 5:
            print(f'{i}..', end='')
else:
    print('O número 5 não aparece na lista')

