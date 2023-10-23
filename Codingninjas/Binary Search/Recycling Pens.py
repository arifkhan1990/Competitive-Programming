# linear soluation 
# def recyclePens(n, r, k, c):
#     if n < r//c:
#         return n
#     elif n == r//c:
#         return n
#     else:
#         return recyclePens(n-1, r+k, k, c)

def recyclePens(n, r, k, c):
    l, h = 0, n
    while l < h:
        m = 1 + l + (h-l) // 2 
        recycleCost = ((n-m)*k)  + r

        if recycleCost < m*c:
            h = m-1
        else:
            l = m
    return l