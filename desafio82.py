lista = []
lista_par = []
lista_impar = []

while True:
    lista.append(int(input('Digite um valor: ')))
    if str(input('Desejar digitar mais um valor? [S/N]')).strip().upper() == 'N':
        break
for i in lista:
    if i%2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print(f'Você digitou os valores: {lista}')
print(f'Lista de valores pares: {lista_par}')
print(f'Lista valores ímpares: {lista_impar}')
