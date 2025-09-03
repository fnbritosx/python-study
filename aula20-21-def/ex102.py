
def fatorial(a, show= False):
    """
    aaa
    """
    from math import factorial
    if show == True:
        for c in range(a, 0, -1):
            if c != 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} =', end=' ')
        print(factorial(a))
    else:
         print(factorial(a))

fatorial(5, True)
help(fatorial)