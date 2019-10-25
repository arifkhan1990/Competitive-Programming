#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 28: RegEx, Patterns, and Intro to Databases
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-regex-patterns/problem
#

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    firstName = []

    for N_itr in range(N):
        firstNameEmailID = input().split()
        emailId = firstNameEmailID[1]
        if emailId.find("@gmail.com") != -1:
            firstName.append(firstNameEmailID[0])

    for i in sorted(firstName):
        print(i)
