#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 14: Scope
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-scope/problem
#

class Difference:
    def __init__(self, a):
        self.__elements = a
    
    def computeDifference(self):
    	self.maximumDifference=max(a)-min(a)

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)