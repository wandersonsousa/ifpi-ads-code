#Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.

def main():
    lado1 = int(input('Lado 1 >> '))
    lado2 = int(input('Lado 2 >> '))
    lado3 = int(input('Lado 3 >> '))

    encontrar_hipotenusa_cateto( lado1, lado2, lado3) 



def encontrar_hipotenusa_cateto(l1, l2, l3):
    if l1 > l2 and l1  > l3:
        print(f'\n Hipotenusa > {l1}\n catetos > {l2} e {l3}')
    elif l2 > l3 and l2 > l1:
        print(f'\n Hipotenusa > {l2}\n catetos > {l1} e {l3}')
    else:
        print(f'\n Hipotenusa > {l3}\n catetos > {l2} e {l1}')


main()