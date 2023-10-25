def searchInsert(arr: [int], m: int):
    n=len(arr)

    low=0

    high=n-1

    ans=n

    while(low<=high):

        mid=(low+high)//2

        if(arr[mid]>=m):

            ans=mid

            high=mid-1

        else:

            low=mid+1

    return ans
