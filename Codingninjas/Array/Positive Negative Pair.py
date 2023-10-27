'''
    Time Complexity     :   O(N)
    Space Complexity    :   O(N)

    Where 'N' is the size of the array.
'''

def pairs(arr, n):

    # Initialize 'visited' array as false.
    visited = [False] * 100000

    v = []

    # For each element in the array, 'arr'.
    for i in range(0, n):
        if arr[i] > 0:
            # Mark 'visited' true for positive values.
            visited[arr[i]] = True

    for i in range(0, n):
        # If seen before, push it in the 'v'.
        if arr[i] < 0 and visited[abs(arr[i])] == True:
            v.append(abs(arr[i]))

    out = [[]]

    for i in range(0, len(v)):
        out.append([-v[i], v[i]])

    return out
