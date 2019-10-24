/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Speed
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
    int n, tc, a;
    scanf("%d",&tc);

    while(tc--) {
        scanf("%d",&n);
        int ans = 1, b;
        scanf("%d",&b);;n--;
        while(n--) {
            scanf("%d",&a);
            if(a<=b) ans++;
            if(b > a) b = a;
        }
        printf("%d\n", ans);
    }
    return 0;
}
