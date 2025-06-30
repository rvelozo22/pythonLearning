num = int((input('Digite um número e te direi se ele é par ou impar: ')))

if num%2 == 0:
    print(f'Você digitou {num} que é um número \033[1;34mPAR!\033[m')
else:
    print(f'O número {num} é \033[1;34mÍMPAR \033[m!')

