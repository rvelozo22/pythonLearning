minimo = 0
maximo = 0

for i in range(1,6):
    peso = float(input('Digite o seu peso: '))
    if i == 1:
        maximo = peso
        minimo = peso
    else:
        if peso < minimo:
            minimo = peso
        if peso > maximo:
            maximo = peso

print('\n')
print(f'\033[33mPESO MÁXIMO: \033[34m{maximo}\033[m', end=' ::::: ')
print(f'\033[33mPESO MÍNIMO: \033[34m{minimo}\033[m')