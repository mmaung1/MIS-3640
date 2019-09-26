def gcd(a,b):
    if b == 0:
        return a
    elif a == 0:
        return b
    elif a > b:
        return gcd(b, a%b)
    else:
        return gcd(a, b%a) # % is a modulus returns remainder after dividin a and b, will have same sign as b rather than a.

print(gcd(24,3))