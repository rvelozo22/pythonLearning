sexo = str(input('Digite seu sexo [M/F]: ')).upper()
if sexo != 'M' and sexo != 'F':
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite seu sexo válido [M/F]: ')).upper()
print('Digitação correta.')

