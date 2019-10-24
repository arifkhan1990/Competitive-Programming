/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Sumita and equal array
               Judge       :   HackerEarth
               Date        :   15/3/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;

int main()
{
   int tc, n , m, x, y,z, sum = 0;
   scanf("%d",&tc);
   while(tc--) {
    scanf("%d %d %d %d",&n,&x,&y,&z);
    bool ans = 0;int p;
    for(int i = 0; i < n ; i++) {
        scanf("%d",&m);

        while(m%x == 0) m /= x;
        while(m%y == 0) m /= y;
        while(m%z == 0) m /= z;
        if(i > 1 and m != p) ans = 1;

        p = m;
    }
    printf((ans? "She can\n":"She can't\n"));
   }

   return 0;
}

