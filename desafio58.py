import random

print('JOGO DE ADVINHAÇÃO.')
num = int(input('Tente acertar o número de 0 a 10 que o computador pensou!'))
ranNum = random.randrange(0,10)
cont = 0

while ranNum != num:
    num = int(input('Errou! Tente novamente: '))
    cont += 1
print(f'Depois de {cont} tentativas, você acertou! Pensamos no número: {ranNum}.')
