lista = []
for i in range(1,6):
    print(f'Digite um número na posição {i}:  ', end ='')
    lista.append(int(input()))
maior = max(lista)
menor = min(lista)

posMaior = []
posMenor = []

for j in range (len(lista)):
    if lista[j] == maior:
        posMaior.append(j)
    if lista[j] == menor:
        posMenor.append(j)
        



if len(posMaior) > 1: 
    print(f'O maior número foi {maior}, nas posições: ', end='')
    for k in posMaior:
        print(k, end='..')
else:
    print(f'O maior número foi {maior}, na posição: ', end='')
    print(f'{posMaior[0]}')



if len(posMenor) > 1: 
    print(f'O menor número foi {menor}, nas posições: ', end='')
    for l in posMenor:
        print(l, end='..')
else:
    print(f'O menor número foi {menor}, na posição: ', end='')
    print(f'{posMenor[0]}')

