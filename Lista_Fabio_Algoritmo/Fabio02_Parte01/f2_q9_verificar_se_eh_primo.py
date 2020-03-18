#Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.

def main():
    if( eh_primo( 0 ) ):
        print('Primo')
    else:
        print('Não é primo')

def eh_primo( n ):
    if( n > 11):
        if( n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0 ):
            return False
        else:
            return True
    else:
        if( n == 2 or n == 3 or n == 5 or n == 7 or n == 11 ):
            return True
        else:
            return False

        


main()