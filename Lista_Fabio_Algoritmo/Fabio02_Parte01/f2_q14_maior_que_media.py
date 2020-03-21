# Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.


def main():
    n1 = int(input('Numero >> '))
    n2 = int(input('Numero >> '))
    n3 = int(input('Numero >> '))
    n4 = int(input('Numero >> '))
    n5 = int(input('Numero >> '))

    media = calc_media(n1, n2, n3, n4, n5)
    printa_num_acima_media(media, n1, n2, n3, n4, n5)


def calc_media(n1, n2, n3, n4, n5):
    return (n1 + n2 + n3 + n4 + n5) / 5


def printa_num_acima_media(media, n1, n2, n3, n4, n5):
    print('\n')
    if n1 > media:
        print('Acima da media >>', n1)
    if n2 > media:
        print('Acima da media >>', n2)
    if n3 > media:
        print('Acima da media >>', n3)
    if n4 > media:
        print('Acima da media >>', n4)
    if n5 > media:
        print('Acima da media >>', n5)


main()
