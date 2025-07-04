a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão ds PA: '))
a10 = a1 + (10*r)
pa = []


for i in range(a1,a10,r):
    pa.append(i)

print('\n')
print('='*80)
print('O resultado da PA descrita é: ',end='')
print(pa)
print('='*80)


        
