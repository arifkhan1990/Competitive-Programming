def gcd(x,y):
   if y == 0:
      return x
   return gcd(y, x%y)

def LCM(x: int, y: int) -> int:
   return x// gcd(x,y)*y