def isValidPair(arr, n, k, m):
    # 6/6 test case pass
    if n%2 != 0:
        return False
    idx = {}
    for i in range(n):
        r = arr[i]%k
        idx[r] = idx.get(r, 0) + 1

    for j in idx:
        nV = (m-j+k)%k

        if idx[j] != idx[nV]:
            return False
    return True


# partitaly test case pass 3/6 timelimit exceeded
    # if n%2 != 0:
    #     return False
    # idx = []
    # for i in range(n):
    #     for j in range(n):
    #         if i!= j and i not in idx and j not in idx and (arr[i] + arr[j])%k == m:
    #             idx.extend([i,j])
    #             # print(arr[i] , arr[j], arr[i] + arr[j] , (arr[i] + arr[j])%k ,m)
    # if len(idx) == n:
    #     return True
    # else:
    #     return False
