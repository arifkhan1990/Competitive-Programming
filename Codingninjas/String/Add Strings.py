'''
    Time complexity: O(|NUM1| + |NUM2|)
    Space complexity: O(1)
    
    Where |NUM1| and |NUM2| are the length of the strings.
'''

def stringSum(num1: str, num2: str) -> str:
    
    # Indices to traverse the strings.
    idx1 = len(num1) - 1
    idx2 = len(num2) - 1
    
    # To store the sum.
    res = ""
    
    # To store the carry.
    carry = 0
    
    # Add characters individually,
    while idx1 >= 0 or idx2 >= 0:
        
        # To store sum of current character.
        localSum = 0
        
        # Check if num1 is present.
        if idx1 >= 0:
            
            # Add current character.
            localSum += int(num1[idx1])
            idx1 -= 1
        
        # Check if num2 is present.
        if idx2 >= 0:
            
            # Add current character.
            localSum += int(num2[idx2])
            idx2 -= 1
        
        # Add carry to the sum.
        localSum += carry
        
        carry = 0
        
        # Check if sum is greater than 9.
        if localSum > 9:
            
            # Update sum and carry.
            localSum %= 10
            carry = 1
        
        # Update the result.
        res += str(localSum % 10)
    
    # If carry is present.
    if carry:
        res += '1'
    
    # Reverse the string.
    res = "".join(reversed(res))
    
    return res