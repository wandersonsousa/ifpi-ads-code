# Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for
# maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso
# contrario, é arredondado para o inteiro imediatamente inferior.


def main():
    numero = int(input("Digite o numero inteiro a ser arredondado >> "))
    decimo = int(input("Digite o decimo do numero >> "))
    print(arredondar(numero, decimo))


def arredondar(num, dec):
    if (dec > 4):
        num += 1
        dec = 0
        return num
    if (dec < 5):
        num -= 1
        dec = 0
        return num


main()
