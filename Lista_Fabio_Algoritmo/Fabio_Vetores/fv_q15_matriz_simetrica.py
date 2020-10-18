# Leia uma matriz quadrada de ordem N e escreva se ela é ou não simétrica. Uma matriz quadrada é dita simétrica se A[i,j] =A[j,i].

N = int(input('N: '))
matriz = []

for i in range(N):
    matriz.append([])
    for j in range(N):
        matriz[i].append( int( input('Valor: ') ) )



def eh_simetrica( matriz ):
    simetrica = True
    for i in range(N):
        for j in range(N):
            if( matriz[i][j] != matriz[j][i] ):
                simetrica = False
    return simetrica

print( eh_simetrica(matriz) )