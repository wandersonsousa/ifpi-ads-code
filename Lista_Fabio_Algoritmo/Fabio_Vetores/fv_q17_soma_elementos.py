# Leia uma matriz quadrada de ordem N e encontre a linha que possui a maior e a menor soma dos elementos.

N = int(input('N: '))
matriz = []

for i in range(N):
    matriz.append([])
    for j in range(N):
        matriz[i].append( int( input('Valor: ') ) )




def maior_linha_em( matriz ):
    maior_linha = 0
    maior_soma = sum(matriz[maior_linha])
    for i in range(N):
        sumLine = sum( matriz[i] )
        if( sumLine > maior_soma ):
            maior_soma = sumLine
            maior_linha = i
    return maior_linha

def menor_linha_em( matriz ):
    menor_linha = 0
    menor_soma = sum(matriz[0])
    for i in range(N):
        sumLine = sum( matriz[i] )
        if( sumLine < menor_soma ):
            menor_soma = sumLine
            menor_linha = i
    return menor_linha

print('matriz', matriz)
print('maior soma é da linha:', maior_linha_em(matriz) + 1 )
print('menor soma é da linha:', menor_linha_em(matriz) + 1 )
