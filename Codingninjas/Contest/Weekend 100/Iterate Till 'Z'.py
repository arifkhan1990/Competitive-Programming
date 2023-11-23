from typing import List

def iterateTillZ(x: int, y: int, z: int) -> List[int]:
    ans = []
    for i in range(1,z+1):
        if i%x == y:
            ans.append(i)
    return ans