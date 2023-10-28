from collections import *
from sys import stdin


def highestOccuringChar(string) :
	c = Counter(string)
	return c.most_common(1)[0][0]

#main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)