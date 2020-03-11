def do_four(d,v):
    do_twice( d, v)
    do_twice( d, v)

def do_twice(f, a):
    f(a)
    f(a)


do_four( print, "ooi" )