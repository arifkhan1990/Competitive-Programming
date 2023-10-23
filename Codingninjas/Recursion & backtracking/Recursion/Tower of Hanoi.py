
def towerOfHanoi(n):
    ans = []
    move( n, 2, 1, ans)
    return ans


def move(n, end, start, ans):
    if n == 1:
        ans.append([start, end])
        return

    other = 1^2^3^end^start
    move(n-1,other, start, ans)
    ans.append([start, end])
    move(n-1, end, other, ans)