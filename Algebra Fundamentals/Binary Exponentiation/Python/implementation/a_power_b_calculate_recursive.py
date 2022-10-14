def binPow(a, b):
    if b == 0:
        return 1
    
    res = binPow(a, b//2)
    if b%2:
        return res*res*a
    else:
        return res*res

a,b = map(int, input().split())
print(binPow(a, b))