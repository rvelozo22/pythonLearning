# print('Bem vindo(a) ao banco RV\n')

# while True: 
#     valor = int(input('Qual valor deseja sacar? '))
#     cinquenta = valor // 50
#     sobra = valor - (cinquenta*50)
#     vinte = sobra // 20
#     sobra = sobra - (vinte*20)
#     um = sobra // 1
#     sobra = sobra - um
#     if sobra == 0:
#         break
# print(f'Serão: \n Cédulas de 50: {cinquenta} \n Cédulas de 20: {vinte} \n Cédulas de 1: {um} ')


# Resolução Guanabara

print('='*30)
print('{:^20}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO CEV')
print('='*30)
