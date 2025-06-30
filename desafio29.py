velMax = 80

velAtual = int(input('A que velocidade o veículo passou? '))

if velAtual > velMax:
    print(f'\nVocê foi multado por ultrapassar {velMax}km/h.\n')
    multa = (velAtual - velMax)*7
    print(f'O valor da multa será de: R${multa:.2f}'.replace('.',','))
else:
    print('\nVelocidade dentro do limite permitido!\n')
