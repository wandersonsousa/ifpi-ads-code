def main():
    angulo = int(input('angulo >> '))

    print( calcula_quadrante(angulo) )


def calcula_quadrante( ang ):
    if ang <= 90 and ang > 0:
        return 'Primero Quadrante'
    elif ang > 90 and ang <= 180:
        return 'Segundo Quadrante'
    elif ang > 180 and ang <= 270:
        return 'Terceiro Quadrante'
    elif ang > 270 and ang <= 360:
        return 'Quarto Quadrante'



main()