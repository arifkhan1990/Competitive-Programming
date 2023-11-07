# 1st solution
''' Optimal
    TC: O(n)
    SC: O(1) '''
def longestSubSeg(arr, n, k):
    #   Write your code here.
    res = left = count = 0

    for right in range(n):
        if arr[right] == 0:
            count += 1
            while count > k:
                if arr[left] == 0:
                    count -= 1
                left += 1
        
        res = max(res, right-left+1)
    return res

# 2nd solution

# '''
# 	Time complexity: O(N)
# 	Space complexity: O(K)

# 	where 'N' is the total number of elements in the array and 'K' is the maximum number of replacements allowed from 0 to 1.
# '''

# from collections import deque

# def longestSubSeg(arr, n, k):

#     # Starting index of array under consideration.
#     l = 0
#     max_len = 0
#     q = deque()
#     # To store current size of the queue.
#     size = 0

#     # i decides current ending point, i.e. the right pointer.
#     for r in range(n):
#         if (arr[r] == 0):
#             q.append(r)
#             size += 1

#         # Updating queue when its size becomes greater than k.
#         if (size > k):
#             # Updating starting index of array under consideration.
#             l = q.popleft() + 1
#             size -= 1

#         max_len = max(max_len, r - l + 1)

#     return max_len