cont = 0
div = 0
tres = False

print('Digite 4 números:\n', end='')
val = tuple((int(input()), int(input()), int(input()), int(input())))


for i in range(len(val)):
    if val[i] == 9:
        cont +=1
    if val[i] == 3:
        tres = True

print(f'O número 9 foi digitado {cont} vez(es)')

if tres == True:
    print(f'O número 3 apareceu primeiro na posição: {val.index(3)}')


print('Os números pares são: ', end='')

for j in range(len(val)):
    div = val[j]%2
    if div == 0:
        print(f'{val[j]}', end=' ')

    
# Resolução Guanabara: 

# num = (int(input('Digite um número: ')),
#        int(input('Digite outro número: ')),
#        int(input('Digite mais um número: ')),
#        int(input('Digite o último número: '))
#        )

# print(f'Você digitou os valores {num}')
# print(f'O valor 9 apareceu {num.count(9)} vez(es)')

# if 3 in num:
#     print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
# else:
#     print('O valor 3 não apareceu nenhuma vez')

# print('Os valores pares digitados foram: ', end='')
# for n in num:
#     if n%2 == 0:
#         print(n, end='')
