pares = []
impares = []
total = []

for i in range(0,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

pares.sort()
impares.sort()
total.insert(0,pares)
total.insert(0,impares)

print(f'Os números pares inseridos foram: {total[1]}')
print(f'Os números ímpares inseridos foram: {total[0]}')