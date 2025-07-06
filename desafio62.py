a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
pa = a1
n = 1
termos = 10
add = 1


print(f'{pa} >> ', end = '')
while add != 0:
    while n < termos:
        pa += r
        print(f'{pa}', end = '')
        print(f' | {n} >> ' if n+1 != termos else '\n', end ='')
        n += 1
    add = int(input('Desejar ver mais quantos termos: '))
    termos = termos + add
print(f'Fim do programa. Foram mostrados {n} termos de uma PA!')