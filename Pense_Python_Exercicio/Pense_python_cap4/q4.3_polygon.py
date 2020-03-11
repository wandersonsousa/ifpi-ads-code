import turtle

bob = turtle.Turtle()
def polygon(t, length, n):
    print( t )
    for i in range(n):
        t.fd(length)
        t.lt( 360/n  )
    turtle.mainloop()  
      

polygon( bob,50, 5)