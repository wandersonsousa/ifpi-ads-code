#Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se dividirmos o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, o quadrado deste terceiro número é exatamente o número original de quatro dígitos. Por exemplo: 
# 2025 -> dividindo: 20 e 25 -> somando temos 45 -> 452 = 2025.

from math import sqrt

def main():
    d1 = str(input('Dígito >> '))
    d2 = str(input('Dígito >> '))
    d3 = str(input('Dígito >> '))
    d4 = str(input('Dígito >> '))

    if atende_a_regra( d1, d2, d3, d4 ):
        print('\nO número atende a regra !')
    else:
        print('\nNão atende a regra.')


def atende_a_regra( n1, n2, n3, n4 ):

    numero_completo = digito_para_numero( n1, n2, n3, n4)
    primeiros_algarismos = digito_para_numero(n1, n2, '', '')
    ultimos_algarismos = digito_para_numero('', '', n3, n4)

    return pow( (primeiros_algarismos + ultimos_algarismos), 2 ) ==  numero_completo

def digito_para_numero( n1 , n2 , n3, n4):
    num_str = n1 + n2 + n3 + n4
    return int(num_str)

main()
 