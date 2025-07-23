matriz = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = (int(input(f'Digite um valor para [{i},{j}]: ')))

print()

pares = 0
coluna = 0
maiorSegLinha = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            pares += matriz[i][j]
        if j == 2:
            coluna += matriz[i][j]
        if i == 1:
            if i == 0:
                maiorSegLinha = matriz[i][j]
            else:
                if matriz[i][j] > maiorSegLinha:
                    maiorSegLinha = matriz[i][j] 
    print()

print()
print(f'A soma dos números pares é: {pares}')
print(f'A soma dos valores da terceira coluna foi de: {coluna}')
print(f'O maior valor da segunda linha foi: {maiorSegLinha}')