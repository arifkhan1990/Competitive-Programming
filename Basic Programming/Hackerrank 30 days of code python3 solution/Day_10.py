#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 10: Binary Numbers
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-binary-numbers/problem
#

print(len(max(bin(int(input().strip()))[2:].split('0'))))