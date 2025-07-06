num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
menu = 0

while menu != 5:
    menu = int(input('''\nEscolha uma opção no menu: \n1 - Somar\n2- Multiplicar
3 - Mostrar maior número \n4 - Digitar novos números
5 - Sair do programa \nOpção: '''))
    match menu:
        case 1:
            soma = num1 + num2
            print(f'\nA soma dos números é: {soma}')
        case 2:
            mult = num1 * num2
            print(f'\nA multiplicação dos dois números é: {mult}')
        case 3:
            if num1 > num2:
                print(f'O maior numero digitado foi: {num1}')
            else:
                print(f'O maior número digitado foi: {num2}')
        case 4:
            num1 = int(input('Digite o primeiro número: '))
            num2 = int(input('Digite o segundo número: '))

print('Você solicitou o fim do programa!')

        
            
          
        