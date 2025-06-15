import math

adj = float(input("Digite o tamanho do cateto adjacente:"))
op = float(input("Digite o tamanho do cateto oposto:"))

print("\nDados do triângulo retângulo:")
print('-'*25)
print(f'Cateto oposto: {op}')
print(f'Cateto adjacente: {adj}')
print(f'Hipotenusa: {math.hypot(op,adj)}')
print('-'*25)