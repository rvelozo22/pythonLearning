num = int(input('Digite um número para saber seu fatorial: '))
aux = num -1
inicial = num

while aux != 0:
    print(f'{num} x {aux} = {num*aux}')
    num = num * aux
    aux -= 1
print(f'\n{inicial}! = {num}')

#Resolução Guanabara: 

# num = int(input('Digite um número para saber seu fatorial: '))
# cont = num
# f = 1 

# print(f'Calculando fatorial de {num}! = ', end ='')
# while cont > 0:
#     print(f' {cont}', end = '')
#     print(f' x ' if cont > 1 else ' = ', end='')
#     f *= cont
#     cont -= 1
# print(f'{f}') 