import datetime

def voto(idade):
    idade = datetime.date.today().year - idade
    
    if idade < 16:
        return(f'Com {idade}: Voto NEGADO!')
    elif (idade >= 16 and idade < 18) or idade >= 65:
        return(f'Com {idade}: Voto OPCIONAL!')
    else:
        return(f'Com {idade}: Voto OBRIGATÓRIO!')
    
ano = int(input('Digite o ano do seu nascimento: '))

print(voto(ano))