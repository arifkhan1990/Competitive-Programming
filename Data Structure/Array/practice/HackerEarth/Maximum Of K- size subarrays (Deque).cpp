/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Maximum Of K- size subarrays (Deque)
               Judge       :   HackerEarth
               Date        :   3/9/19
               Time        :   O(N*K)
               Memory      :   676KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n, k;
    scanf("%d %d",&n,&k);
    int ar[n+1] = {0};

    for(int i = 0; i < n; i++) {
        cin >> ar[i];
    }

    for(int i = 0; i <= n - k; i++) {
        int mx = 0;
        for(int j = 0;  j < k; j++) {
            mx = max(mx, ar[i+j]);
        }
        cout << mx << " ";
    }
    return 0;
}
