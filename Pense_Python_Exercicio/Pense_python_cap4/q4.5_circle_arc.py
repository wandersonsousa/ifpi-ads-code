import turtle
# Faça uma versão mais geral do circle chamada arc, que receba um parâmetro adicional de angle, para determinar qual fração do círculo deve ser desenhada. angle está em unidades de graus, então quando angle=360, o arc deve desenhar um círculo completo.

bob = turtle.Turtle()
pi = 3.14
def polygon(t, n, ang_final):
    length = 1
    print( t )     
    for i in range( n ):
        if( i == ang_final):
            break
        t.fd(length)
        t.lt( 360 / n  )
    turtle.mainloop()

def arc( t, r, a):
    n = int(2 * pi * r )
    ang_final = (n * a ) // 360
    print(ang_final)
    print(n)
    polygon(t, n, ang_final)

arc( bob, 50, 360)


