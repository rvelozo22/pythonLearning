in1 = input('Digite o que vier na sua mente:')

if in1.isnumeric():
    print('Você digitou um número')
elif in1.isalpha():
    print('Você digitou apenas letras')
elif in1.isalnum():
    print('Você digitou letras e números')
elif in1.isupper():
    print('Você digitou em letras maiúsculas')
else:
    print('Você digitou algo que não posso identificar!')
    