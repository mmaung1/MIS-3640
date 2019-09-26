def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b) # % is a modulus returns remainder after dividin a and b, will have same sign as b rather than a.

print(gcd(2,12))