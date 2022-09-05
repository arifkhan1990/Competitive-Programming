def solveNQ(n):
    col = set()
    posDiag = set() # r+c
    negDiag = set() # r-c
    
    ans = []
    board = [['0'] * n for _ in range(n)]
    
    def backtraking(r):
        if r == n:
            copy = ["".join(r) for r in board]
            ans.append(copy)
            return
        
        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue
            
            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = "Q"
            
            backtraking(r+1)
            
            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = "0"
    backtraking(0)
    return ans


print(solveNQ(4))
            