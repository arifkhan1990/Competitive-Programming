/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Takeoff
               Judge       :   HackerEarth
               Date        :   3/9/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
    #include<bits/stdc++.h>
    using namespace std;

    bool takeOff(int n, int p,int q, int r) {
       if(n%p == 0 and n%q != 0 and n%r != 0) return 1;
       if(n%p != 0 and n%q != 0 and n%r == 0) return 1;
       if(n%p != 0 and n%q == 0 and n%r != 0) return 1;
       return 0;
    }

    int main()
    {
        int n, p , q, r, tc, ans = 0;
        scanf("%d",&tc);

        while(tc--) {
            ans = 0;
            scanf("%d %d %d %d",&n ,&p ,&q ,&r);

            for(int i = 1; i <= n ; i++) if(takeOff(i,p,q,r)) ans++;
            printf("%d\n", ans);

        }
        return 0;
    }
