#Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. Lembre-se de que o valor da área não pode ser negativo.

from math import sqrt, pow

def main():
    print('Cordenada primeiro ponto')
    x1 = int(input('X >> ')) 
    y1 = int(input('Y >> ')) 

    print('Cordenada segundo ponto')
    x2 = int(input('X >> ')) 
    y2 = int(input('Y >> ')) 


    print( 'Área >> ',calcular_base(x1, y1, x2, y2) )


def calcular_base(x1, y1, x2, y2):
    altura_retangulo = abs( y2 - y1 )
    base_retangulo = abs( x2 - x1 )
    return base_retangulo * altura_retangulo


main()