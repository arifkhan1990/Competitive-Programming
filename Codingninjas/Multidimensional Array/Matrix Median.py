def getMedian(matrix):
    ans = []
    for i in range(len(matrix)):
        ans.extend(matrix[i])
    
    ans.sort()
    return ans[len(ans)//2]
