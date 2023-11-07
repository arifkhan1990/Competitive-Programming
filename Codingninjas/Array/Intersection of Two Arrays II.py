import sys

def intersections(arr1, n, arr2, m) :

    for i in arr1:
        if i in arr2:
            arr2.remove(i)
            print(i, end=" ")