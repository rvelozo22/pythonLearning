index = [1,2,3,4,5,6,7,8,9,10]
in1 = int(input('Digite um número inteiro: '))

print('\nA tabuada de {} é:'.format(in1))

print("-"*13)
for i in index:
    result = in1*i
    print(f"{in1} x {i:2} = {result}")
print("-"*13)

