#Leia uma matriz quadrada de ordem N, calcule e escreva a soma dos elementos da diagonal principal, a soma dos elementos da diagonal secundária e a soma dos elementos que não estão na diagonal principal nem na diagonal secundária

N = int(input('N: '))
matriz = []

diagonal_principal = 0
diagonal_secundaria = 0
outros = 0

posicao_diagonal_principal = 0
posicao_diagonal_secundaria = N - 1
posicao_outros = 0

for i in range(N):
    matriz.append([])
    for j in range(N):
        matriz[i].append( int( input('Valor: ') ) )
        if( j == posicao_diagonal_principal ):
            diagonal_principal += matriz[i][j]
        elif( j == posicao_diagonal_secundaria ):
            diagonal_secundaria += matriz[i][j]
        else:
            outros += matriz[i][j]

    posicao_diagonal_principal += 1
    posicao_diagonal_secundaria -= 1

print('\nmatriz:', matriz)
print('valor diagonal principal:', diagonal_principal )
print('valor diagonal secundária:', diagonal_secundaria)
print('outros elementos:', outros)