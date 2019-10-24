/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Sumit's love for maths
               Judge       :   HackerEarth
               Date        :   15/3/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
   ll n, a, b, c, ans, x, y ,z,p,tc;
   scanf("%lld",&tc);

   while(tc--) {
   scanf("%lld %lld %lld %lld",&n,&a,&b,&c);

   ans = (n/a) + (n/b) + (n/c);

   x = (a*b)/ (__gcd(a,b));
   y = (a*c)/ (__gcd(a,c));
   z = (c*b)/ (__gcd(c,b));
   p = (x*c)/ (__gcd(x,c));

   ans -= (n/x) + (n/y) + (n/z);
   ans +=  (n/p);

   printf("%lld\n",ans);
   }
   return 0;
}

