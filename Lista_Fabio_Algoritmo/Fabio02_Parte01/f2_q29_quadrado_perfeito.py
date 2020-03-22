#Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas formadas pelos seus dois primeiros e dois últimos dígitos.Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito. Escreva um algoritmo que leia um número de 4 dígitos e verifique se ele é um quadrado perfeito.

from math import sqrt

def main():
    d1 = str(input('Dígito >> '))
    d2 = str(input('Dígito >> '))
    d3 = str(input('Dígito >> '))
    d4 = str(input('Dígito >> '))

    if eh_quadrado_perfeito( d1, d2, d3, d4 ):
        print('\nÉ um quadrado perfeito que atende a regra !')
    else:
        print('\nNão atende a regra.')


def eh_quadrado_perfeito( n1, n2, n3, n4 ):

    numero_completo = digito_para_numero( n1, n2, n3, n4)
    primeiros_algarismos = digito_para_numero(n1, n2, '', '')
    ultimos_algarismos = digito_para_numero('', '', n3, n4)

    return sqrt( numero_completo ) == (primeiros_algarismos + ultimos_algarismos)

def digito_para_numero( n1 , n2 , n3, n4):
    num_str = n1 + n2 + n3 + n4
    return int(num_str)

main()
 