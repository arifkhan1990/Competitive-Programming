from os import *
from sys import *
from collections import *
from math import *


def maximumInAllSubarraysOfSizeK(arr, n, k):
    # Declare an empty array to store maximum of all k sized subarrays
    answer = []

    #Declare an empty deque to maintain a window of indices
    indexWindow = []

    # Run a loop and iterate through all elements of the array
    for i in range(n):

        # If the front element of the deque is out of bound from the current window then remove it
        if (len(indexWindow) != 0 and indexWindow[0] == i - k):
            indexWindow.pop(0)

        # Remove the rightmost indices of deque until the element at this index is smaller than
        # The current element i.e. arr[i]
        while (len(indexWindow) != 0 and arr[i] > arr[indexWindow[-1]]):
            indexWindow.pop(-1)

        # Push index of current element to window
        indexWindow.append(i);

        # If size of window is greater than k then add
        # Element having index equals to front element of deque
        # To answer
        if (i >= k - 1):
            answer.append(arr[indexWindow[0]])

    # Return the answer
    return answer
    