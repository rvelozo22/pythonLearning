alunos = []
nome = []
notas = []

while True: 
    nome.insert(0, str(input('Nome: ')).strip().capitalize())
    notas.insert(0,float(input('Nota 1: ')))
    notas.insert(1,float(input('Nota 2: ')))
    nome.insert(1,notas[:])
    alunos.insert(0,nome[:])
    nome.clear()
    notas.clear()
    if str(input('Deseja continuar? [S/N] ')).strip().upper() == 'N':
        break

print('-'*40)
print(f'{'No':<10}', end ='')
print(f'{'Nome':<20}', end ='')
print(f'{'Média'}')
print('-'*40)

soma = 0

for i in range(len(alunos)):
    print(f'{i:<10}', end ='')
    print(f'{alunos[i][0]:<20}', end ='')
    for j in range(len(alunos[i][1])):
         soma += alunos[i][1][j]
    media = soma / 2
    soma = 0
    print(f'{media}')

while True:
    select = int(input('Deseja ver as notas de qual aluno? 999 para interromper!'))
    if select == 999:
        break
    print()
    print(f'{alunos[select][0]}', end = ' ')
    print(' ----> ', end='')
    print(f'{alunos[select][1]}')
    

# print(alunos)
