# Leia uma matriz quadrada de ordem N e encontre a linha que possui a maior e a menor soma dos elementos.

N = int(input('N: '))
matriz = []

for i in range(N):
    matriz.append([])
    for j in range(N):
        matriz[i].append( int( input('Valor: ') ) )




def maior_linha_em( matriz ):
    maior_linha = sum(matriz[0])
    for line in matriz:
        if( sum(line) > maior_linha ):
            maior_linha = sum(line)
    return maior_linha

def menor_linha_em( matriz ):
    menor_linha = sum(matriz[0])
    for line in matriz:
        if( sum(line) < menor_linha ):
            menor_linha = sum(line)
    return menor_linha
    

print('maior soma de linha:', maior_linha_em(matriz) )
print('menor soma de linha:', menor_linha_em(matriz) )
