import time

def cont_1():
    print('~'*25)
    print('Contando de 1 até 10 de 1 em 1: ')
    for i in range (1,11):
        print(i, end=' ', flush = True)
        i += 1
        time.sleep(0.5)
    print()

def cont_2():
    print('~'*25)
    print('Contando de 10 até 0 de 2 em 2: ')
    for j in range(10,-1,-2):
        print(j, end=' ', flush=True)
        time.sleep(0.5)
    print()

def cont_3(ini, fim, passo):
    if ini > fim and passo > 0:
        passo = passo * -1
    elif passo == 0:
        passo = 1

    if passo < 0:
        print(f'Contando de {ini} até {fim} de {passo*-1} em {passo*-1}: ')
        fim = fim - 1
    else:
        print(f'Contando de {ini} até {fim} de {passo} em {passo}: ')
        fim = fim + 1

    for k in range(ini, fim, passo):
        print(k, end=' ', flush=True)
        time.sleep(0.5)


#cont_1()

#cont_2()

print('~'*25)
print('Personalize sua contagem')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

cont_3(inicio, fim, passo)
