    /*
                 ...........................................................

                   Solver      :   Arif Khan
                   Problem     :   ArrayGame
                   Judge       :   HackerEarth
                   Date        :   14/3/19
                   Time        :   O(N)
                   Memory      :   64KB
                   Difficulty  :   Easy

                 ...........................................................
    */
    #include<bits/stdc++.h>
    using namespace std;

    int main()
    {
        int n, m;
        scanf("%d %d",&n,&m);
        long long ans = 0;
        int ar[n+1] = {0},br[m+1] = {0};
        for(int i = 0; i < n; i++) scanf("%d",&ar[i]);
        for(int i = 0; i < m; i++) scanf("%d",&br[i]);
        sort(ar,ar+n);
        sort(br,br+m,greater<int>());

        for(int i = 0;i < m and i < n; i++) {
            if(ar[i]<br[i]) ans += br[i] - ar[i];
        }
        printf("%lld\n",ans);
        return 0;
    }
