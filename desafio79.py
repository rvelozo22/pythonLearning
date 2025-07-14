lista = []

while True: 
    n = int(input('Digite um número: '))
    if n in lista:
        print('Valor já digitado, tente outro valor')
    else:
        lista.append(n)
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break
print('Você digitou os números: ', end='')
for i in range(len(lista)):
    if i == (len(lista) - 1):
        print(f'{lista[i]}')
    else:
        print(f'{lista[i]}', end=', ')
