matriz = [[[],[],[]], [[],[],[]], [[],[],[]]]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j].append(int(input(f'Digite um valor para [{i},{j}]: ')))

print()

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j != len(matriz[i])-1:
            print(f'[{matriz[i][j][0]:^5}]', end='')
        else:
            print(f'[{matriz[i][j][0]:^5}]')

