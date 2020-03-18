#Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; ovalor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores possíveis para a variável opção são 1, 2 e 3.

def main( ):
    opcao = int( input('Opção >> ') )
    printar_num( opcao, 2, 4, 6 )

def printar_num( op, n1, n2, n3 ):
    if( op > 0 and op <= 3  ):
        if op == 1:
            print( n1)
        if op == 2:
            print(n2)
        if op == 3:
            print(n3)
    else:
        print('opcao invalida')

main()