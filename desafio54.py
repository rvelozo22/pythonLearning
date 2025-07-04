from datetime import date
cont = 0
anoAtual = date.today().year

print(anoAtual)

for i in range(1,8):
    anoNascimento = int(input('Digite o ano de seu nascimento: '))
    if anoAtual - anoNascimento >= 21:
        cont += 1
print(f'Das 7 pessoas, {cont} já atingiram a maioridade')
