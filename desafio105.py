def notas(*nota, sit=False):
    """
    -> Analisa nota inputadas
    :param nota: Pode receber várias notas
    :param sit: (opcional) retorna ou não a situação do aluno (aprovado, reprovado ou recuperação)
    :return: retorna um dicionário com: quantidade de notas, maior nota, média e situação (opcional)
    """
    aluno = {}
    aluno['total'] = len(nota)
    aluno['media'] = sum(nota)/len(nota)
    aluno['maior'] = max(nota)
    aluno['menor'] = min(nota)
    # n = 0
    # for i in range(len(nota)):
    #     if i == 0:
    #         aluno['maior'] = nota[i]
    #     else:
    #         if nota[i] >aluno['maior']:
    #             aluno['maior'] = nota[i]
    #     n += nota[i]
    #     aluno['total'] += 1
    # aluno['media'] = n/len(nota)
    if sit == True:
        if aluno['media'] >= 7:
            aluno['situacao'] = 'APROVADO'
        elif aluno['media'] >= 5 and aluno['media'] < 7:
            aluno['situacao'] = 'RECUPERAÇÃO'
        else:
            aluno['situacao'] = 'REPROVADO'
    
    return aluno


print(notas(5.5,2,10,8.5, sit=True))

