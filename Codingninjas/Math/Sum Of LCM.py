def gcd(a, b):
    if b == 0:
        return a
    return gcd(b,a%b)

def lcmSum(n):
    ans = 0
    for i in range(1, n+1):
        gcdV = gcd(i,n);
        lcm = (i*n) // gcdV
        ans += lcm
    return ans
