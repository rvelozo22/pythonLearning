cont = soma = 0 
while True:
    n = int(input('Digite um número de 0 a 998. Para parar o programa, digite 999. '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados {cont} número(s) e soma entre eles é de: {soma}')