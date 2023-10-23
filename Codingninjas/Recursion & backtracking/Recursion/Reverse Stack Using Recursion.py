from typing import List

def reverseStack(stack: List[int]) -> None:
    if len(stack) == 0:
        return
    print(stack.pop(), end=" ")
    reverseStack(stack)