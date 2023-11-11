from os import *
from sys import *
from collections import *
from math import *




def lps(unsorted_str, sorted_str , l1, l2, ans):
    if l1 == 0 or l2 == 0:
        return 0

    if ans[l1][l2] != -1:
        return ans[l1][l2]
    
    if unsorted_str[l1-1] == sorted_str[l2-1]:
        ans[l1][l2] = 1 + lps(unsorted_str, sorted_str, l1-1,l2-1, ans)
        return ans[l1][l2]
    else:
        ans[l1][l2] = max(lps(unsorted_str,sorted_str, l1-1, l2, ans), lps(unsorted_str, sorted_str, l1,l2-1, ans))
        return ans[l1][l2]

def longestPalindromeSubsequence(s):
    ans = [[-1 for i in range(1001)] for j in range(1001)]
    l = len(s)
    unsorted_str = s
    sorted_str = unsorted_str[::-1]
    res = lps(s, sorted_str, l, l, ans)
    return  res


# '''
#     Time complexity: O(2 ^ N)
#     Space complexity: O(N)

#     Where 'N' is the length of the string.
# '''

# '''
#     Returns the length of the longest palindromic subsequence
#     in the string s between index i and j.
# '''
# def longestPalindromeSubsequenceHelper(s, i, j):
    
#     # Base Case 1: If there is only 1 character.
#     if (i == j):
#         return 1
    
#     # Base Case 2: If there are only 2 characters and both are same.
#     if(s[i] == s[j] and i + 1 == j):
#         return 2
    
#     # If the first and last characters match.
#     if(s[i] == s[j]):
#         return longestPalindromeSubsequenceHelper(s, i + 1, j - 1) + 2
    
#     # If the first and last characters do not match.
#     op1 = longestPalindromeSubsequenceHelper(s, i, j - 1)
#     op2 = longestPalindromeSubsequenceHelper(s, i + 1, j)
    
#     return max(op1, op2) 

# # Returns the length of the longest palindromic subsequence in the string s.
# def longestPalindromeSubsequence(s):
    
#     return longestPalindromeSubsequenceHelper(s, 0, len(s) - 1)
