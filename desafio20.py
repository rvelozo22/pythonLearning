import random 

al1 = input('Insira o nome do primeiro aluno: ')
al2 = input('\nInsira o nome do segundo aluno: ')
al3 = input('\nInsira o nome do terceiro aluno: ')
al4 = input('\nInsira o nome do quarto aluno: ')

lista = [al1, al2, al3, al4]

random.shuffle(lista)

print('-'*50)
print('A ordem de apresentação será:\n')
for i, nome in enumerate(lista, 1):
    print(f'{i}º aluno(a) - {nome}')
print('-'*50)
