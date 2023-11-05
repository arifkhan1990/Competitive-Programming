# approach 1

def longestValidParentheses(s):
    ans = 0
    l ,r = 0 , 0
    for i in range(len(s)):
        if s[i] == ')':
            r += 1
        else:
            l += 1
        
        if l == r:
            ans = max(ans, l+r)
        elif r > l:
            l, r = 0, 0
    l,r = 0, 0
    for i in s[::-1]:
        if i == '(':
            l += 1
        else:
            r += 1
        
        if l == r:
            ans = max(ans, l+r)
        elif l > r:
            l, r = 0, 0
    return ans


#  approache  2
'''
	Time complexity: O(N)
	Space Complexity: O(N)
	
	Where N is the size of the given string.
'''

# def longestValidParentheses(s):
#     ans = 0

#     stk = []
#     stk.append(-1)

#     for i in range(len(s)):

#         if (s[i] == '('):
#             # Push the current index.
#             stk.append(i)
#         else:
#             stk.pop()
#             if (len(stk) == 0):
#                 # Push the current index.
#                 stk.append(i)
#             else:
#                 # Found a valid substring. So, find its length.
#                 l = i - stk[len(stk) - 1]

#                 # Update the answer, if required.
#                 ans = max(ans, l)
                        
#     return ans