/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Strange Game
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
        int tc, n , m;
        scanf("%d",&tc);
        while(tc--) {
            scanf("%d %d",&n, &m);
            long long al[n+1], bo[n+1];
            long long bmx = 0, ans = 0;
            for(int i = 0; i < n ; i++) cin >> al[i];
            for(int i = 0; i < n ; i++) {
                cin >> bo[i];
                bmx = max(bmx, bo[i]);
            }

            for(int i = 0; i < n ; i++) {
                ans += ((bmx >= al[i])? bmx - al[i] + 1 : 0)*m;
            }
            cout << ans << endl;
        }
        return 0;
    }
