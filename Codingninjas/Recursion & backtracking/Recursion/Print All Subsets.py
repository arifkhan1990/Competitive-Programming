def solve(arr, i, n , subPro):
    if n == i:
        if len(subPro) > 0:
            print(*subPro, sep = ' ')  
        return
    
    solve(arr, i+1, n, subPro)
    solve(arr, i+1, n, subPro+arr[i:i+1])

def printAllSubsets(n, arr):
    ans = []
    solve(arr, 0,n,[])
