# Leia um número (vetor com 8 elementos) na base binária, calcule e escreva este número na base hexadecimal e na base decimal.
number_bin = input()
number_bin_list = list( map( int, [n for n in number_bin] ) )

def bin_to_dec( binary_list ):
    dec = 0
    binary_reversed = binary_list[::-1]
    for i in range(len(binary_reversed)):
        bin = binary_reversed[i]
        dec += bin * 2 ** i
    return dec


def dec_to_hex( dec ):
    hex = ''
    digits = "0123456789ABCDEF"
    result = []

    while( dec > 0 ):
        remainder = dec % 16
        dec = dec // 16

        result.append( digits[ remainder ] )

    return ''.join( result[::-1] )


print('Em binário:', bin_to_dec( number_bin_list ))
print('Em hexadecimal:', dec_to_hex( bin_to_dec( number_bin_list ) )  )