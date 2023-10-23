
def numOfPartitions(arr, m):
    t, nP = 0, 1
    for i in arr:
        t += i
        if t > m:
            t = i
            nP += 1
    return nP


def findLargestMinDistance(boards:list, k:int):
    l, h = max(boards), sum(boards)

    while l < h:
        m = l + (h-l) // 2
        reqPartition = numOfPartitions(boards, m)
        if reqPartition <= k:
            h = m
        else:
            l = m+1
    return l



# Driver code
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print(int(findLargestMinDistance(arr, k)))