# Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda
# for 1 escreva a soma dessas variáveis mais o resto da divisão;
#  se for 2 escreva se o primeiro e o
# segundo valor são pares ou ímpares;
#  se for igual a 3 multiplique a soma dos valores lidos pelo
# primeiro; se for igual a 4divida a soma dos números lidos pelo segundo, se este for diferente de
# zero. Em qualquer outra situaçãoescreva o quadrado dos números lidos.


def main():
    valor1 = int(input('Valor >> '))
    valor2 = int(input('Valor >> '))

    resto = valor1 % valor2
    
    if resto == 1:
        print( (valor1 + valor2) + resto )

    elif resto == 2:
        if( eh_par(valor1) ):
            print('valor1 é par')
        else:
            print('valor1 é impar')
        
        if( eh_par(valor2) ):
            print('valor2 é par')
        else:
            print('valor2 é impar')

    elif resto == 3:
        resultado = (valor1 + valor2) * valor1
        print( resultado )

    elif resto == 4:
        resultado = (valor1 + valor2) / valor2
        print( resultado )

    elif resto != 0:
         print( valor1 ** 2, valor2 ** 2)


def eh_par(n):
    return n % 2 == 0







main()


