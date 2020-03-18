#Leia 1 (um) número inteiro e escreva se este número é par ou impar.

def main():
    num = int( input('Numero >> ') ) 

    if( eh_par(num) ):
        print('Par')
    else:
        print('impar')


def eh_par( n ):
    return n % 2 == 0

main()