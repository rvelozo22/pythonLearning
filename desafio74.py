from random import randint
list = []

for i in range(0,5):
    num = randint(0,200)
    list.append(num)

tupla = tuple((list))

for j in range(len(tupla)):
    if j == 0:
        maior = tupla[j]
        menor = tupla[j] 
    if tupla[j] < menor:
        menor = tupla[j]
    if tupla[j] > maior:
        maior = tupla[j]

print(f'Os números sorteador foram: {tupla}')
print(f'\nO maior número é: {maior}')
print(f'\nO menor número é: {menor}')

# Resolução Guanabara

# num = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
# print('Os valores sorteados foram: ', end='')
# for i in num:
#     print(f'{i} ', end='')

# print(f'\nO maior valor foi: {max(num)}')
# print(f'O menor valor foi: {min(num)}')