valorImovel = float(input('Digite o valor do imóvel em reais: '))
renda = float(input('Digite sua renda bruta em reais: '))
qtdPrestacoes = int(input('Digite em quantos meses pretende pagar o imóvel: '))
maxParcelas = renda*0.3

print(f'\nO valor das parcelas não pode ultrapassar {maxParcelas}.')

parcelas = valorImovel/qtdPrestacoes

if maxParcelas > parcelas:
    print(f'\nFinancimanto aprovado. Você pagará {qtdPrestacoes} prestações de R$ {parcelas:.2f}!')
else:
    print(f'\nFinanciamento reprovado. O valor da prestação supera 30% de sua renda bruta')