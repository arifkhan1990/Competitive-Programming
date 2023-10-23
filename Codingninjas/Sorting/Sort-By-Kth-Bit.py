def sortArrayByKBit(n, k, arr):
    ans1= []
    ans2= []
    k  -= 1

    for x in arr:
        if x & (1<<k):
            ans1.append(x)
        else:
            ans2.append(x)
    return ans2 + ans1