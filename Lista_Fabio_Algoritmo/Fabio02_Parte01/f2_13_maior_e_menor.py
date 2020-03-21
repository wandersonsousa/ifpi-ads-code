# Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são diferentes.


def main():
    n1 = int(input('Numero >> '))
    n2 = int(input('Numero >> '))
    n3 = int(input('Numero >> '))
    n4 = int(input('Numero >> '))
    n5 = int(input('Numero >> '))

    pega_maior_e_menor(n1, n2, n3, n4, n5)


def pega_maior_e_menor(n1, n2, n3, n4, n5):
    maior = n1
    menor = n1

    if(n2 > maior):
        maior = n2
    else:
        menor = n2

    if n3 > maior:
        maior = n3
    elif n3 < menor:
        menor = n3

    if n4 > maior:
        maior = n4
    elif n4 < menor:
        menor = n4

    if(n5 > maior):
        maior = n5
    elif n5 < menor:
        menor = n5

    print('Maior número >>', maior)
    print('Menor número >>', menor)


main()
