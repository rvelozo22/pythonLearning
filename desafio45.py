import random

jogadasPc = ['pedra', 'papel', 'tesoura']

print('Vamos jogar JOKENPO!')
print('-'*30)
jogador = str(input('Escolha uma das opções:\n- Pedra\n- Papel\n- Tesoura\n\n'))
print('-'*30)

pc = random.choice(jogadasPc)

jogador = jogador.lower()

if jogador in (jogadasPc):
    if jogador == pc:
        print(f'\nPC jogou \033[34m{pc.title()}\n\n\033[33mEMPATE\033[m!')
    elif (jogador == 'papel' and pc == 'pedra') or (jogador == 'tesoura' and pc == 'papel') or (jogador == 'pedra' and pc == 'tesoura'):
        print(f'\nPC jogou \033[34m{pc.title()}\n\n\033[32mVITÓRIA\033[m!')
    else:
        print(f'\nPC jogou: \033[34m{pc.title()}\n\n\033[31mDERROTA\033[m!')    
else:
    print('Jogada inválida')

