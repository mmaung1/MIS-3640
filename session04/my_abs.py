def my_abs(a):  #parameter needs to be defined because in the body, a is already stored as a temporary variable
    if a >= 0:
        print(a)
    else:
        print(-a)

my_abs(2) #but here you can put any number you want and it will replace the parameter that is stored as a temporary variable
my_abs(-2)

def brian_abs(number):
    if isinstance(number, int):

        if number >= 0:
            return number
        else:
            return -number
    else:
        return 'I don\'t know'

