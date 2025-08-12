def leiaFloat(msg):
    while True:
        print(msg, end='')
        try:
            val = input().strip()
            val = float(val.replace(",", "."))
            
        except (ValueError, TypeError):
            print('ERRO! Número real inválido!')
            continue
        except KeyboardInterrupt:
            return 0
        else:
            return val
        
def leiaInt(msg):
    while True:
        print(msg, end='')
        try:
            val = input().strip()
            val = int(val)
            
        except (ValueError, TypeError):
            print('ERRO! Número inteiro inválido!')
            continue
        except KeyboardInterrupt:
            return 0
        else:
            return val
        

inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O número inteiro foi: {inteiro} e o real foi: {real}')