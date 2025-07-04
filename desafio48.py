s = 0
v = 0
for i in range(1,501):
    if i%3 == 0:
        d = i/3
        if d%2 == 1:
            v += 1
            s += i
print(f'A soma dos {v} valores é igual a: {s}')
