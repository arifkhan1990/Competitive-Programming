def binPow(a, b):
    res = 1
    while b > 0:
        if b&1 :
            res *= a
        a *= a
        b >>= 1
    return res
    
a,b = map(int, input().split())
print(binPow(a, b))