index = [1,2,3,4,5,6,7,8,9,10]
in1 = int(input('Digite um número inteiro:'))

print('A tabuada de {} é:'.format(in1))

for i in index:
    result = in1*i
    print(f"{in1} x {i} = {result}")


