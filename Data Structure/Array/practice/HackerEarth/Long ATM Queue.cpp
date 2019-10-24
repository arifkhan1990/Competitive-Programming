/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Long ATM Queue
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
        int n,ans = 0;
        cin >> n;
        int ar[n+1] = {0};
        cin >> ar[0];
        for(int i = 1; i <= n; i++) {
            cin >> ar[i];
            if(ar[i] < ar[i-1]) ans++;
        }

        cout << ans << endl;
        return 0;
    }

