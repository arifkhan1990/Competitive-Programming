    /*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Memorise Me!
               Judge       :   HackerEarth
               Date        :   3/9/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Very-Easy

             ...........................................................
*/

    #include<bits/stdc++.h>
    using namespace std;

    int main()
    {
        int n,a,q;
        scanf("%d",&n);
        int ar[1001] = {0};

        for(int i = 0; i < n; i++) {
            scanf("%d",&a);
            ar[a]++;
        }
        scanf("%d",&q);
        while(q--) {
            scanf("%d",&a);
            if(ar[a] == 0) printf( "NOT PRESENT\n");
            else printf("%d\n",ar[a]);
        }

        return 0;
    }
