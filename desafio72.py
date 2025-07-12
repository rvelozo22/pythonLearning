num  = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
num_str = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', ' dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

index = int(input('Digite um número entre 0 e 20: '))
while index < 0 or index > 20:
    print('Número inválido. Tente novamente.')
    index = int(input('Digite um número entre 0 e 20: '))

resposta = num.index(index)
print(f'Você digitou o número {num_str[resposta]}')


#Resolução Guanabara

# num_str = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', ' dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# while True:
#     num = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= num <= 20:
#         break
#     print('Tente novamente.', end=' ')
# print(f'Você digitou o número {num_str[num]}')