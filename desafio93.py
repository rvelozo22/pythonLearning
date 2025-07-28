jogador = {}
gols = []
c_gols = 0

jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
partidas = int(input('Quantas partidas o jogador jogou na última semana? '))

for i in range(0,partidas):
    gols.insert(i, int(input(f'Gols na partida {i+1}: ')))

jogador['gols'] = gols[:]

for i in (jogador['gols']):
    c_gols += i
jogador['total'] = c_gols

print('-='*50)
print(jogador)
print('-='*50)

for k, v in jogador.items():
    print(f'{k:<10} ---> {v}')
print('-='*50)

print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')
for j,k in enumerate(jogador['gols']):
    print(f'  ==> Partida {j+1}, fez {k} gol(s)')
print(f'Um total de {jogador['total']} gol(s)')