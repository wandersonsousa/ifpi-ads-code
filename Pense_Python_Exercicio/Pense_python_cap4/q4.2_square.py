import turtle

bob = turtle.Turtle()
def square(t,length):
    print( t )
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()  
      
square( bob,40 )