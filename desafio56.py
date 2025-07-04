somaIdade = 0
idadeHomem = 0
contIdade = 0

for i in range(1,5):
    nome = str(input('Qual o seu nome: '))
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Seu sexo: M ou F: '))
    sexo = sexo.upper()
    somaIdade += idade

    if sexo == 'M':
        if idade > idadeHomem:
            homemVelho = nome
    else:
        if idade < 20:
            contIdade += 1

print('\n')
print('='*25)
print(' '*7, end='')
print('Dados do grupo:')
print('='*25)
print('\n')

print(f'\033[34mMédia de idade:\033[m {somaIdade/4:.2f}')
print(f'\033[34mNome do homem mais velho: \033[m{homemVelho}')
print(f'\033[34m{contIdade}\033[m mulher(es) tem menos de 20 anos')

print('\n')
print('='*25)