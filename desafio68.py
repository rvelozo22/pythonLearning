import random

while True:
    escolha = str(input('Escolha par ou ímpar: [P/I] ')).strip().upper()
    num = int(input('Escolha um número de 1 a 10: '))
    if num >= 1 and num <= 10:
        pc = random.randint(1,10)
        result = (pc + num)%2
        if escolha == 'P':
            if result == 0:
                vitoria = True
            else:
                vitoria = False
        if escolha == 'I':
            if result == 1:
                vitoria = True
            else:
                vitoria = False
        if vitoria == False:
            break
        else:
            print(f'Você venceu, você jogou {num} e o computador {pc}.')
            print('Vamos jogar novamente!\n')
    else:
        print('Número inválido, tente novamente\n')
print(f'Você perdeu. O computador jogou {pc} e você {num}. Tente novamente mais tarde')
