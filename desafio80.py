lista = []
for i in range(0,5):
    n = int(input('Digite um número: '))
    if len(lista) == 0:
        lista.append(n)
    #     pos = 1
    else:
    
        for j in range(len(lista)):
            # print(n-lista[j])
        
            if n > lista[j]:
                pos = j+1
            if n < lista[j]:
                if n < lista[j-1]:
                    pos = j -1
                else:
                    pos = j
            if n == lista[j]:
                pos = j
                break
        lista.insert(pos,n)
        print(f'Item inserido na posição: {pos}')
    # print(f'O item foi inserido na posição: {pos}')
print(lista)


