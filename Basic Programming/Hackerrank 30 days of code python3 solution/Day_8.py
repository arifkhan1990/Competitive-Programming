#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 8: Dictionaries and Maps
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
#

from sys import stdin

if __name__ == "__main__":
    lines = stdin.read().splitlines()
    
    databook = dict(i.split() for i in lines[1:int(lines[0])+1])
    
    print('\n'.join(["{0:}={1:}".format(i,databook[i]) if i in databook else "Not found" for i in lines[int(lines[0])+1:]]))