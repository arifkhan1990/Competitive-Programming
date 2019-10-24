/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Most Frequent
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
    int n, a;
    cin >> n;
    int br[10] = {0}, ans = 0;
    for(int i = 0; i < n; i++) {
        cin >> a;
        int ar[10] = {0};
        while(a != 0) {
            int p = a%10;
             a /= 10;
             if(ar[p] == 0) br[p]++, ar[p] = 1;
        }

        for(int i = 0; i < 10; i++) {
            ans = max(ans,br[i]);
            }
        }
    cout << ans << endl;
    return 0;
}
