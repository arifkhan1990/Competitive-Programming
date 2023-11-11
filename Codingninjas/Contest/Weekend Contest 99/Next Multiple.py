
def nextMultiple(n: int, m: int) -> int:
    if n < m:
        return m
    else:
        while n%m:
            n += 1
    return n