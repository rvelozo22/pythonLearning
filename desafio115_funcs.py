def cadastrar():
    print('='*50)
    try:
        nome = str(input('Nome: ')).strip().title()
        idade = int(input('Idade: '))
        with open("cadastro.txt", "a") as file:
            if file.tell() != 0:
                file.write('\n')
            file.write(f"{nome:<35}{idade:0>2} anos")
    except IOError:
        print('Não foi possível escrever no arquivo')
    else:
        print(f'O registro de {nome} foi cadastrado com sucesso')

def ler():
    try: 
        with open("cadastro.txt", "r") as file:
            conteudo = file.read()
    except IOError:
        print('Não foi possível ler o arquivo')
    except FileNotFoundError:
        print('O arquivo não existe!')
    else:
        print('='*50)
        print(f'{"PESSOAS CADASTRADAS":^40}')
        print('='*50)
        return conteudo

