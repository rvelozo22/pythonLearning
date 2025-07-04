frase = str(input('Digite uma frase para verificar se é um palindromo: '))
frase = frase.replace(' ', '').lower().strip()
tamanho = len(frase)
j = tamanho
cont = 0

for i in range(0, tamanho):
    j = j -1 
    if frase[i] == frase[j]:
        cont += 1
if cont == tamanho:
    print('A frase é um palindromo!')
else:
    print('A frase não é um palindromo!') 
