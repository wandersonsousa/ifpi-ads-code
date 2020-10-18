# Leia um vetor A com N elementos, verifique e escreva se existem ou não elementos iguais no vetor.

N = int(input('N: '))
A = []
for i in range(N):A.append( int( input('Valor: ') ) )

def hasEqual( array ):
    for element in A:
        hasEqual = False
        for i in range( len(A) ):
            if element == A[i]:
                if( hasEqual ): return True
                hasEqual = True
    return False
    
print( hasEqual( A ) )