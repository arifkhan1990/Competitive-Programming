
def factorial(n):
    assert n >= 0, 'Number must be positive integer'

    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))