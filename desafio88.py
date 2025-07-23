from random import sample

n = 0 
lista = []
final = []

for i in range(0,60):
    n += 1
    lista.append(n)

print('='*30)
print(f'{'MEGA SENA':^30}')
print('='*30)
print()

jogos = int(input('Quantos jogos deseja gerar? '))

for j in range(0, jogos):
    mega = sample(lista, k = 6)
    mega.sort()
    final.append(mega)

for j in range(len(final)):
    print(f'Jogo {j+1}: ', end ='')
    for l in range(len(final[j])):
        print(final[j][l], end = ' ')
    print()


