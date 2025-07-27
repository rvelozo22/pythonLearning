aluno = dict()


aluno['Nome'] = str(input('Nome do aluno(a): '))
aluno['Media'] = float(input('Média do aluno(a): '))
if aluno['Media'] >= 7:
    aluno['Status'] =  'Aprovado(a)'
else:
    aluno['Status'] = 'Reprovado(a)'

print(f'A média de {aluno['Nome']} foi de {aluno['Media']}, e ele(a) está {aluno['Status']}')    