cont = 0 
continuar = ''
soma = 0

while continuar != 'N':
    num = int(input('Digite um número inteiro: '))
    soma += num
    continuar = str(input('Deseja digitar mais um número? [S/N] ')).strip().upper()
    while continuar != 'N' and continuar != 'S':
        continuar = str(input('Opção inválida, tente novamente. Deseja continuar? [S/N] ')).strip().upper()
    cont += 1
    
print(f'\nVocê digitou {cont} valores. A média deles é: {soma/cont}')
