ano = int(input('Digite o ano para saber se é bissexto: '))

def bissexto(ano):
    if ano%4 == 0:
        if ano%100 == 0:
            if ano%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if bissexto(ano):
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto!')


