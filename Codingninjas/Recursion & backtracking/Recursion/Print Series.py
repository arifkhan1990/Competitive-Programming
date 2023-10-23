def printSeries(n, k):
    ans = []
    Fseries(n,k,ans)
    return ans+ans[:-1][::-1]

def Fseries(n,k, ans):
    ans.append(n)
    if n <= 0:
        return ans
    
    return Fseries(n-k,k,ans)

