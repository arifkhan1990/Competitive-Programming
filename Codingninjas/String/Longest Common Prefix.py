def longestCommonPrefix(arr, n):
    ans = arr[0] 
    l = len(ans)

    for i in range(1, n):
        while arr[i].find(ans) != 0:
            ans = ans[:l-1]
            l -= 1
    return ans