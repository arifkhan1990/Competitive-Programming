
def matchSpecificPattern(words, n, pattern):
    res = []

    for s in words:
        if len(s) == len(pattern) and len(set(s)) == len(set(pattern)):
            ans = {}
            b = 1
            for i, j in zip(pattern, s):
                if ans.get(i):
                    if ans[i] != j:
                        b = 0
                        break
                else:
                    ans[i] = j

            if b == 1:
                res.append(s)

    return res