from collections import *

def relativeSorting(arr, brr, n, m):
    ans = []
    stock = defaultdict(int)

    for i in range(n):
        stock[arr[i]] += 1

    for i in range(m):
        if brr[i] in stock:
            count = stock[brr[i]]
            while count:
                ans.append(brr[i])
                count -= 1
            del stock[brr[i]]
            
    if not stock:
        return ans
    index = len(ans)
    
    for key, value in stock.items():
        while value:
            ans.append(key)
            value -= 1
    ans[index:] = sorted(ans[index:])
    return ans



