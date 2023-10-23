
def solve(inputStack, N, c):
    if c == N:
        inputStack.pop()
        return 
    ans = inputStack.pop()
    solve(inputStack, N, c+1)
    inputStack.append(ans)
    return inputStack

def deleteMiddle(inputStack, N):
    solve(inputStack, N//2, 0)
    return inputStack