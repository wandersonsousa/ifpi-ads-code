#Leia um vetor com N elementos, encontre e escreva o maior e o menor elemento e suas respectivas posições no vetor.

N = int(input('N: '))
vetor = []
for i in range(N):vetor.append( int( input('Valor: ') ) )

def bigger_element( vetor ):
    bigger = vetor[0]
    for n in vetor:       
        if( n > bigger ):
            bigger = n

    return bigger

def smaller_element( vetor ):
    smaller = vetor[0]
    for n in vetor:     
        if( n < smaller ):
            smaller = n

    return smaller

print('maior:', bigger_element( vetor ) )
print('menor:', smaller_element( vetor ) )