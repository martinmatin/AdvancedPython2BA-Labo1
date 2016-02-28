# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016
from math import sqrt

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    if n <0:
        raise ValueError('Il faut un entier supérieur ou égal à 0')
    if n==0:
        return 1
    if n >0:
        a = n
        while n > 1:
            n = n-1
            a = a*n
        return a
def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    
    delta = (b**2)-(4*a*c)
    if delta < 0:
        t =()
        return t
    if delta ==0:
        r = (-b/(2*a))
        t = r
        return t
    if delta > 0:
        ra = (-b + (sqrt(delta)))/(2*a)
        rb = (-b - (sqrt(delta)))/(2*a)
        t = (ra, rb)
        return t
        
        
             

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    return "5"

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))


    #""
