n = int(input('Digite o número de termos da sequência de Fibonacci: '))
cont = 0
result = 0
fibonacci = []

while cont <= n-1:
    if cont == 0:
        result = 0
    elif cont == 1:
        result = 1
    else:
        result =  fibonacci[cont-1] + fibonacci[cont-2]
    print(f'{result}', end='')
    print(' >> ' if (cont != n-1) else '', end='' )
    fibonacci.append(result)
    cont += 1
print(f'\n{fibonacci}')
    

# Resolução Guanabara
# Para digitar a seta pro lado, ativar numLock e apertar ALT+26 (Só funciona com teclado alfanumérico)

# n = int(input('Quantos termos você quer mostrar? '))
# t1 = 0
# t2 = 1

# print(f'{t1} → {t2}', end ='')
# cont = 3
# while cont <= n:
#     t3 = t1 + t2
#     print(f' → {t3}', end='')
#     t1 = t2
#     t2 = t3
#     cont += 1
# print(' → FIM!') 