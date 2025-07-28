pessoas = []
dados = {}
soma_id = 0
mulheres = []
acima_media = []
pessoa_acima_media = {}

while True:
    dados['nome'] = str(input('Nome: ')).strip().capitalize()
    dados['sexo'] = str(input('Sexo: [M/F]')).strip().upper()
    while True:
        if dados['sexo'] in 'MF':
            break
        else:
            print('ERRO! Digite apenas M ou F!')
            dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    while True:
        if continuar in 'SN':
            break
        else:
            print('ERRO! Digite apenas S ou N!') 
            continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break


for i in range(len(pessoas)):
    soma_id += pessoas[i]['idade']
    if pessoas[i]['sexo'] == 'F':
        mulheres.append(pessoas[i]['nome'])

media_id = soma_id/len(pessoas)    

for j in range(len(pessoas)):
    if pessoas[j]['idade'] > media_id:
        acima_media.append(pessoas[j].copy())

print('-='*50)
print(f'A) Foram cadastradas {len(pessoas)} pessoas;')
print(f'B) A média de idade é de {media_id:.1f}')
print(f'C) As mulheres cadastradas foram: ',end ='')
for i in mulheres:
    print(i,end='..')
print()
print(f'D) As pessoas com idade acima da média foram: ')
for k in acima_media:
    for prop,v in k.items():
        print(f'  {prop.capitalize()}: {v}', end=';')
    print()
