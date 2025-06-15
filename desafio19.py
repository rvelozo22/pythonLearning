import random

al1 = input('Digite o nome do aluno 1: ')
al2 = input('\nDigite o nome do aluno 2: ')
al3 = input('\nDigite o nome do aluno 3: ')
al4 = input('\nDigite o nome do aluno 4: ')

print('-'*75)
print(f'O aluno sorteado para resolver o exercício foi: {random.choice([al1, al2, al3, al4])}')
print('-'*75)