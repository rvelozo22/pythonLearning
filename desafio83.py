exp = str(input('Digite uma expressão matemática: '))

cont1 = 0
cont2 = 0

for i in exp:
    if i in '(':
        cont1 += 1
    if i in ')':
        cont2 += 1

if cont1 == cont2: 
    print('Expressão válida!')
else:
    print('Expressão inválida!')

# Solção Guanabara

# expr = str(input('Digite uma expressão matemática: '))
# pilha = []
# for i in expr:
#     if expr in '(':
#         pilha.append('(')
#     elif expr in ')':
#         if len(pilha) > 0:
#             pilha.pop()
#         else:
#             pilha.append(')')
#             break

# if len(pilha) == 0: 
#     print('Sua expressão é válida')
# else:
#     print('Sua expressão não é válida')