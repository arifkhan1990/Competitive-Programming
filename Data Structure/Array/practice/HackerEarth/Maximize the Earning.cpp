/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Maximize the Earning
               Judge       :   HackerEarth
               Date        :   3/9/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
    #include<iostream>
    using namespace std;

    int main()
    {
        int S, N, R, h,h1, ans = 0;
        scanf("%d",&S);
        while(S--) {
            scanf("%d %d",&N, &R);
            scanf("%d",&h);
            ans = R;
            for(int i = 1; i < N; i++) {
                scanf("%d",&h1);
                if(h < h1) ans += R, h = h1;
            }
            cout << ans << endl;
        }
        return 0;
    }

