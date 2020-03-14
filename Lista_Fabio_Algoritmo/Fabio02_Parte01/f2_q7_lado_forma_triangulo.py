#Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3(três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).

def main():
    gerar_triangulo( 16, 20, 30)



def gerar_triangulo( lado1, lado2, lado3):
    if( forma_triangulo(lado1, lado2, lado3) ):
        print('Não pôde formar o triângulo')

    elif( eh_equilaro(lado1, lado2, lado3) ):
        print("Triângulo Equilátero Formado")

    elif( eh_isosceles(lado1, lado2, lado3) ):
        print("Triângulo Isósceles Formado")
    
    else:
        print("Triângulo Escaleno Formado")
    
def forma_triangulo(l1, l2, l3):
    return l2 + l3 <= l1 or l3 + l1 <= l2 or l1 + l2 <= l3

def eh_equilaro( l1, l2, l3):
    return l1 == l2 == l3
    
def eh_isosceles(l1, l2, l3):
    if( l1 == l2 ):
        return True
    elif( l2 == l3):
        return True
    elif( l1 == l3 ):
        return True
    else:
        return False


main()