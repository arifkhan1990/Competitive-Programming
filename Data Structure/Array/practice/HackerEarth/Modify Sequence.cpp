/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Modify Sequence
               Judge       :   HackerEarth
               Date        :   10/3/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long n, a, mx = 0, mn = INT_MAX;
    scanf("%lld",&n);
    for(int i = 0; i < n; i++) {
        scanf("%lld",&a);
        if(i%2 == 0) mx += a;
        else mx -= a;
    }
    cout << ((mx%11 == 0) ? "YES" : "NO") << endl;
    return 0;
}
