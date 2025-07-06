n = 0
cont = 0
result = 0
while n != 999:
    n = int(input('Digite um número inteiro de 0 a 998. Para parar, digite 999: '))
    if n !=  999:
        cont += 1
        result += n
print(f'Você digitou {cont} número(s). E o resultado da soma entre eles é: {result}')
