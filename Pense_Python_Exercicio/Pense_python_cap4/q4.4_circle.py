import turtle
# Escreva uma função chamada circle que use o turtle, t e um raio r como parâmetros e desenhe um círculo aproximado ao chamar polygon com um comprimento e número de lados adequados. Teste a sua função com uma série de valores de r.Dica: descubra a circunferência do círculo e certifique-se de que length * n = circumference.

bob = turtle.Turtle()
pi = 3.14
def polygon(t, n):
    length = 1
    print( t )  
    for i in range( n ):
        t.fd(length)
        t.lt( 360 / n  )
    turtle.mainloop()
      

def circle( t, r ):
    n = int(r * 2 * pi)
    polygon(t, n)

circle( bob, 1000 )
