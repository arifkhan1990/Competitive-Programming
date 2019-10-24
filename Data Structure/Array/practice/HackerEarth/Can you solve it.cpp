/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Can you solve it ?
               Judge       :   HackerEarth
               Date        :   3/9/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n, tc;
    scanf("%d",&tc);

    while(tc--) {
    scanf("%d",&n);
    int mx1 = 0, mx2 = 0, mn1 = INT_MAX, mn2 = INT_MAX, a ;
    for(int i = 1; i <= n; i++) {
        scanf("%d",&a);
        mx1 = max(mx1, a+i);
        mn1 = min(mn1, a+i);
        mx2 = max(mx2, a-i);
        mn2 = min(mn2, a-i);
        }
        printf("%d\n",max(mx1 - mn1, mx2 - mn2));
    }
    return 0;
}
