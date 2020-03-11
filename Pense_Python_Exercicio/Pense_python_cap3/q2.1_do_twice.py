def do_twice(f):
    f()
    f()

def print_spam():
    print("Hello")

do_twice( print_spam )