from functools import lru_cache

@lru_cache()
def fib(a,b,n):
    if n == 0:
        return 1
    if a+b < n:
        return fib(b, a+b, n)
    elif a+b == n:
        return 1
    else:
        return 0

def checkMember(n):
    return fib(0,1,n)

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")