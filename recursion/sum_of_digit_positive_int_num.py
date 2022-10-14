
def digit_sum(n):
    assert n >= 0 and int(n) == n, 'Number must be positive integer'

    if n < 10:
        return n
    else:
        return n%10 + digit_sum(n//10)

print(digit_sum(30))