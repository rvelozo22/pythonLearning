import math

angulo = float(input('Digite um ângulo para descobrir seu seno, cosseno e tangente: '))

print(f'\nA seguir, seno, cosseno e tangente do ângulo de {angulo}:\n')
print('='*40)
print(f'Seno = {math.sin(math.radians(angulo)):.3f}')
print(f'Cosseno = {math.cos(math.radians(angulo)):.3f}')
if angulo != 90.0:
    print(f'Tangente = {math.tan(math.radians(angulo)): .3f}')
else:
    print('A tangente de 90 não é definida!')
print('='*40)