import datetime

dados = dict()

dados['nome'] = str(input('Nome: ')).strip().capitalize()
dados['idade'] = datetime.date.today().year - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho. (Se não tiver --> 0): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Digite seu ano de contratação: '))
    dados['salario'] = float(input('Informe o salário: '))
    apos = dados['idade'] + (35 - (datetime.date.today().year - dados['contratacao']))
    if apos >= 0:
        dados['aposentadoria'] = apos
    else:
        dados['aposentadoria'] = 0

print(dados)
for k, v in (dados.items()):
    if dados['ctps'] != 0: 
        print(f'{k.capitalize():<15} ---> {v:<15:.2f}')
    else:
        if k != 'ctps':
            print(f'{k:<15} ---> {v:<15.2f}')
