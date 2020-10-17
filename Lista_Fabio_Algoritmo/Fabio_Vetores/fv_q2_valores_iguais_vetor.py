# Leia um vetor A com N elementos, verifique e escreva se existem ou não elementos iguais no vetor.

A = [1,2,4,5,6,7,8,9,10, 11]


def hasEqual( array ):
    for element in A:
        hasEqual = False
        for i in range( len(A) ):
            if element == A[i]:
                if( hasEqual ): return True
                hasEqual = True
    return False
    
print( hasEqual( A ) )