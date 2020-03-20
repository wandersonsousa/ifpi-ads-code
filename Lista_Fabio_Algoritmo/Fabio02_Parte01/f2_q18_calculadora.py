def main():
    valor1 = int(input('valor >> '))
    valor2 = int(input('valor >> '))
    operacao = int(input('operacao [1-4] a, s, m, d >> '))
    print( calculadora( valor1, valor2, operacao ) )




def calculadora( n1, n2, operacao ):
    if( operacao == 1):
        return n1 + n2
    elif( operacao == 2):
        return n1 - n2
    elif( operacao == 3):
        return n1 * n2
    elif( operacao == 4 ):
        return n1 / n2
    else:
        print('Operacao invalida, escolha entre [1-4]')


main()