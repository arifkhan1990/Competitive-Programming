"""Problem: Compute x^n mod m. This is a very common operation. For instance it is used in computing the modular multiplicative inverse.

Solution: Since we know that the module operator doesn't interfere with multiplications (a.b == (a mod m).(b mod m) (mod m)), we can directly use the same code,
 and just replace every multiplication with a modular multiplication:"""

def binPow(a, b, m):
    res = 1
    while b > 0:
        if b&1 :
            res = res*a % m
        a = a*a % m
        b >>= 1
    return res

a,b = map(int, input().split())
print(binPow(a, b, 9999))