phrase = str(input('Digite uma frase: '))

phrase = phrase.lower()

print('\n')
print(f'A letra A aparece {phrase.count('a')} vez(es) na frase\n')
print(f'A primeira vez que A aparece é na posição: {phrase.find('a')}\n')
print(f'A última vez que A aparece é na posição: {phrase.rfind('a')}\n')
