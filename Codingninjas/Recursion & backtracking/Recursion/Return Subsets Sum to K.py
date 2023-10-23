def solve(arr, i, n ,k, ans, subPro):
    if n == i:
        if k == 0:
            ans.append(subPro)
        return ans
    
    solve(arr, i+1, n, k, ans, subPro)
    solve(arr, i+1, n,k-arr[i],ans, subPro+arr[i:i+1])

def findSubsetsThatSumToK(arr, n, k) :
    ans = []
    solve(arr, 0,n, k,ans,[])
    return ans