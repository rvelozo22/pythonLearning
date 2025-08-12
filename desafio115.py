from time import sleep
import desafio115_funcs

while True:
    print('='*50)
    print(f'{"MENU PRINCIPAL":^40}')
    print('='*50)
    print('\033[33m 1 - Visualizar cadastros \n 2 - Novo cadastro \n 3 - Sair do programa\033[m')
    print('='*50)
    try:
        opcao = int(input('Sua opção: '))
    except (ValueError, TypeError):
        print('='*50)
        print('\033[31mDigite uma opção válida\033[m')
        print('='*50)
        sleep(2)
    else: 
        match opcao:
            case 1:
                print(desafio115_funcs.ler())
                print('='*50)
                sleep(2)
            case 2:
                desafio115_funcs.cadastrar()
                print('='*50)
                sleep(2)
            case 3:
                print('Saindo do programa. Até logo...')
                sleep(2)
                break
    
