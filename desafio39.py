from datetime import date

ano = int(input('Digite o ano de seu nascimento: '))

idade = date.today().year - ano

if idade == 18:
    print(f'Você tem {idade} anos e precisa se apresentar ao Serviço Militar!')
elif idade > 18: 
    print(f'Você tem {idade} anos e precisaria ter se apresentado a {idade - 18} ano(s)')
else:
    print(f'Você tem {idade} anos e só precisará se apresentar daqui {18 - idade} ano(s)')