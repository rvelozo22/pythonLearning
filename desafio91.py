from random import randint
import time 

jogadores = {}
ordem = []


for i in range(1,7):
    jogadores[i] = randint(1, 6)


for k, v in jogadores.items():
    print(f'O jogador {k}, tirou {v}')
    time.sleep(1)

for j in jogadores.items():
    if j[0] == 1 or j[1] < ordem[-1][1]:
        ordem.append(j[:])
    else:
        cont = 0
        while cont < len(ordem):
            if j[1] >= ordem[cont][1]:
                ordem.insert(cont, j)
                break
            cont += 1            

print()

for k in range(len(ordem)):
    print(f'{k+1}º --> Jogador{ordem[k][0]} com {ordem[k][1]}')
    time.sleep(1)


# Resolução do Guanabara

# from random import randint
# from time import sleep
# from operator import itemgetter

# jogo = {'Jogador 1': randint(1,6),
#         'Jogador 2': randint(1,6),
#         'Jogador 3': randint(1,6),
#         'Jogador 4': randint(1,6),
#         'Jogador 5': randint(1,6),
#         'Jogador 6': randint(1,6),
# }

# ranking = {}

# print('Valores sorteados: ')

# for k, v in(jogo.items()):
#     print(f'{k} tirou {v} no dado')
#     sleep(1)

# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print('='*30)
# print('  == RANKING DOS JOGADORES ==  ')

# for i, v in enumerate(ranking):
#     print(f'  {i+1}º lugar: {v[0]} com {v[1]}')
#     sleep(1)
