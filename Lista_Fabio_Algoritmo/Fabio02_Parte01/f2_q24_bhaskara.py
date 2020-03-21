#Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas raízes. Vale lembrar que o coeficiente A deve ser diferente de 0 (zero).

def main():
    a = int(input('A >> '))
    b = int(input('B >> '))
    c = int(input('B >> '))

    bhaskara(a, b, c) 



def bhaskara(a, b, c):
    from math import sqrt
    delta = (b ** 2) - (4 * a * c)
    r1 = ( -b + sqrt(delta) ) / 2 * a
    r2 = ( -b - sqrt(delta) ) / 2 * a
    print(f'raiz 1: {r1} \nraiz 2: {r2}')


main()