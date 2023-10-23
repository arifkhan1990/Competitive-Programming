
def sumInRanges(arr, n, queries, q):

    pS = [0]
    for i in range(n):
        pS.append(pS[-1]+arr[i])

    ans = []

    for x in queries:
        s = x[0] - 1
        e = x[1]

        s1 = (pS[-1] * (s//n)) + pS[s%n]
        s2 = (pS[-1] * (e//n)) + pS[e%n]

        ans.append((s2-s1)% (10**9 + 7))
        
    return ans
    