from typing import List

def countMoves(n: int, a: List[int]) -> int:
    odd_moves = 0
    divisible_by_3_moves = 0
    di = []
    ans  = 0
    for i in a:
        if i&1 == 0:
            odd_moves += 1
        if i%3 != 0:
            di.append(i)
            divisible_by_3_moves += 1
    for j in di:
        ans += 3 - (j%3)
    return min(odd_moves, ans)