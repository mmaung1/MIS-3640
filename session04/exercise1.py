import math
def quadratic():
    a = float(input("Please enter a coefficient:"))
    b = float(input("please enter another coefficient:"))
    c = float(input("Please enter another coefficient:"))
    x = (-b+(b**2-4*a*c)**(1/2))/(2*a)
    x2nd = (-b-(b**2-4*a*c)**(1/2))/(2*a)
    print('The value of x are {:.2f} and {:.2f}'.format(x, x2nd))
quadratic()