n = int(input('Digite um número para saber se é ou não um número primo: '))
primo = False
soma = 0

for i in range(1,n+1):
        if n%i == 0:
            soma += 1
if soma == 2:
      print(f'O número {n} é \033[34mPRIMO\033[m!')
else:
      print(f'O número {n} \033[34mNÃO É PRIMO\033[m')