def fatorial(n, sh=False):
    """
    -> Cálcula fatorial de um número n
    param n: número inteiro a se calcular fatorial
    param sh: se deseja mostrar todo o processo de cálculo, então True
    return: fatorial calculado
    """

    f = 1
    final = ''
    for i in range(n,0,-1):
        f *= i

    if sh == True:
        for i in range(n,0,-1):
            if i != 1:
                resp = str(f'{i} X' + ' ')
            else:
                resp = str(f'{i} =' + '')
            final += resp
        final = str(f'{final} ' + str(f))
    else:
        final = str(f'{n}! = {f}')
    return final

# numero = int(input('Digite um número para calcular o fatorial: '))
# if str(input('Deseja mostar o processo de cálculo? [S/N] ')).strip().upper() == 'S':
#     show = True
# else:
#     show = False

# print(fatorial(numero, show))

help(fatorial)