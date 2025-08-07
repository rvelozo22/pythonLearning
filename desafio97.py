def escreva(frase):
    frase = str('  ' + frase + '  ')
    tamanho = len(frase)
    print('~'*tamanho)
    print(frase)
    print('~'*tamanho)

while True:
    user_frase = str(input('Escreva uma frase: ')).strip()
    escreva(user_frase)
    if str(input('Deseja escrever outra frase? [S/N]')).strip().upper() == 'N':
        break


