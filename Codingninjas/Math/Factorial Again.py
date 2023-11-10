'''
    Time Complexity : O((N - P)*log(N))
    Space Complexity : O(1)

    Where 'N' is the number given and 'P' is the given prime number.
'''


def power(x, y, p):

    res = 1  # Initialize result
    x = x % p  # Update x if it is more than or equal to p

    while y > 0:
        # If y is odd, multiply x with result
        if (y & 1) == 1:
            res = (res * x) % p

        # y must be even now
        y = y >> 1  # y = y / 2
        x = (x * x) % p

    return res


def modInverse(a, p):
    return power(a, p - 2, p)


def modMultiplication(a, b, m):
    a = a % m
    b = b % m

    return (((a * b) % m) + m) % m


def modDivision(a, b, m):
    a = a % m
    b = b % m

    return (modMultiplication(a, modInverse(b, m), m) + m) % m


def factorialAgain(n, p):
    n = modMultiplication(n, 3, p)

    res = (p - 1)

    for i in range(n + 1, p):
        res = (res * modInverse(i, p)) % p

    den = 1
    den = power(6, n // 3, p)

    ans = modDivision(res, den, p)

    return ans