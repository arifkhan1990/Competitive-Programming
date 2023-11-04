
def costCal(az,za,ch1,ch2):
    if ch1 == 'z':
        x = az + ord(ch2) - ord('a')
    else:
        x = ord('z') - ord(ch1)
        x += az
        x += ord(ch2) - ord('a')

    if ch1 == 'a':
        y = za + ord('z') - ord(ch2)
    else:
        y = ord(ch1) - ord('a')
        y += za
        y += ord('z') - ord(ch2)
    return [x, y]
    
def makeStringsEqual(n: int, a: int, b: int, s: str, t: str) -> int:
    ans = 0
    for j in range(n):
        if s[j] != t[j]:
            idx = abs(ord(s[j]) - ord(t[j]))
            k = costCal(a,b,s[j],t[j])
            ans += min([k[0],k[1],idx])
    return ans