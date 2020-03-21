def main():
    altura = int( input('Digite sua altura >> ') )
    peso = int( input('Digite seu peso >> ') )

    imc = ( peso / ( altura ** 2 ) )

    print( analisar_imc(imc) )




def analisar_imc( imc ):
    if( imc < 25 ):
        return 'Peso normal'
    elif imc >= 25 and img < 30:
        return 'Obeso'
    elif imc > 30:
        return 'Obesidade Mórbida'


main()