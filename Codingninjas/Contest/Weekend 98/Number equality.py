def canSheMakeEqual(x: int, y: int) -> int:
    if x == y:
        return 1
    return 1 if abs(x-y)%3 == 0 else 0