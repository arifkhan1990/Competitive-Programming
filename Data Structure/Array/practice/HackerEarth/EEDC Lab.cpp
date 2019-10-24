;/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   EEDC Lab
               Judge       :   HackerEarth
               Date        :   3/9/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;

long long ans[1000001] = {0},data[100001] = {0};

int numRevrse(int n) {
    int res = 0;
    while(n != 0) {
         res = n%10  + (res*10);
         n /= 10;
    }
    return res;
}

void alter(long long ar[],long n)
{
    long long num = 0, a, m;
    for(int i = 1; i <= n; i++) num = ar[i] + num*10;

    num = numRevrse(num);
    for(int i = 1; i <= n ; i++) {
      a = num%10;
      num /= 10;

      if((m+numRevrse(num))%2 == 0 and (m+numRevrse(num))%3 == 0 and (m+numRevrse(num))%5 == 0)ans[i] = ans[i-1] + 1;
      else ans[i] = ans[i-1];
      m = a + (m*10);
   }
}

int main()
{
   long long tc, n , m = 0, x = 1, y, sum = 0, a, b, q;

   cin >> n ;

   for(int i = 1; i <= n ; i++) {
        scanf("%lld",&data[i]);
        sum += data[i];
   }
   if(sum > 9) {
      for(int i = 1; i <= n ; i++) {
         x = sum - data[i];
         if(x%3 == 0) {
            if((data[i-1] + data[n])%10 == 0){
               ans[i] = ans[i-1] + 1;
            }else ans[i] = ans[i-1];
         }else ans[i] = ans[i-1];
     }
   }else {
       alter(data, n);
   }
   scanf("%lld",&b);
   while(b--) {
    long long s, e;
    scanf("%lld %lld",&s,&e);
    long long int res = ans[e] - ans[s-1];

    cout << res << endl;
   }

   return 0;
}


