time = []
jogador = {}
gols = []


while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    partidas = int(input('Quantas partidas o jogador jogou na última semana? '))

    for i in range(0,partidas):
        gols.insert(i, int(input(f'Gols na partida {i+1}: ')))

    jogador['gols'] = gols[:]

    cont_gols = 0
    for i in gols:
        cont_gols += i
    jogador['total'] = cont_gols

    time.append(jogador.copy())
    gols.clear()

    while True:
        continuar = str(input('Deseja continuar? [S/N]')).strip().capitalize()
        if continuar in 'SN':
            break
        else:
            print('ERRO! Digite S ou N')
    if continuar == 'N':
        break

print('=-'*40) 

print(f'{"Cód.":<7}', end='')
print(f'{"Jogador":<10}', end='')
print(f'{"Gols":<10}', end='')
print(f'{"Total":<10}')


for c, v in enumerate(time):
    print(f'{c:<7}', end='')
    print(f'{v['nome']:<10}',end='')
    print(f'{str(v['gols']):<10}', end='')
    print(f'{v['total']:<10}')

print('-='*40)

while True:
    sel_jogador = int(input('Mostrar os dados de qual jogador? [999 para encerrar] '))
    if sel_jogador == 999:
        break
    for i, j in enumerate(time[sel_jogador]['gols']):
        print(f'Na partida {i+1} marcou: {j} gol(s)')

