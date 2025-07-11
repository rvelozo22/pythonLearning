cont = 0
caro = 0
cheaper = 0
total = 0


while True:
    nome = str(input('Qual o nome do produto? ')).strip()
    preco = float(input('Qual o valor do produto? '))
    cont += 1
    total += preco
    if preco > 1000:
        caro += 1
    if cont == 1:
        cheaper = nome
        menor_preco = preco
    else:
        if preco < menor_preco:
            cheaper = nome
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break
print('='*45)
print('Fim da compra! Vamos para o resumo: ')
print('='*45)
print('\n')

print(f'O total da compra foi de: {total}')
print(f'O produto mais barato foi: {cheaper}')
print(f'{caro} produto(s) custaram mais de R$1.000\n')
