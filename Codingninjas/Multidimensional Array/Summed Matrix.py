from os import *
from sys import *
from collections import *
from math import *

def query(n, q):
    if q <= n+1:
        return q-1
    else:
        return (n-(n-(n+n-q))+1)
