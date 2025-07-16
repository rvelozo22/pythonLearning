dados = []
pessoas = []
pesados = []
leves = []
cont = 0

maisPesado = maisLeve = 0


while True:
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    if str(input('Deseja coontinuar? [S/N]')).strip().upper() == 'N':
        break

for i, v in enumerate(pessoas):
    if i == 0:
        maisLeve = v[1]
        maisPesado = v[1]
    if v[1] > maisPesado:
        maisPesado = v[1]
    if v[1] < maisLeve:
        maisLeve = v [1]

for i in pessoas:
    if i[1] == maisPesado:
        pesados.append(i)
    if i[1] == maisLeve:
        leves.append(i)
    cont += 1




print(f'Foram cadastradas {cont} pessoas')
print(f'Os mais pesados tem {maisPesado}, são eles: {pesados}')
print(f'Os mais leves tem {maisLeve}, são eles: {leves}')
