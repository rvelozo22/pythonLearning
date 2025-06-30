distLonga = 200
tarifa1 = 0.45
tarifa2 = 0.5
passagem = 0

print(f'\nPara viagens acima de {distLonga}km o valor da tarifa será de R$ {tarifa2:.2f}/km'.replace('.',',')) 
print(f'Viagens menores que essa distância tarifa de R$ {tarifa1:.2f}/km'.replace('.',','))

distancia = int(input('\nDigite a distância, em kilometros, da viagem para eu calcular a passagem: '))


if distancia > distLonga:
    passagem = distancia*tarifa2
    print(f'\nValor total da viagem: R$ {passagem:.2f}'.replace('.',','))
else:
    passagem = distancia*tarifa1
    print(f'\nValor total da viagem: R${passagem:.2f}'.raplace('.', ','))