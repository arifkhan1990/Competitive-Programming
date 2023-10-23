def kthChildNthGeneration(n, k):
    return 'Female' if solve(n,k) else 'Male'

def solve(i, j):
    if i ==1 or j == 1:
        return 0
    
    if j%2 == 0:
        return not solve(i-1, j//2)
    else:
        return solve(i-1,(j+1) // 2)