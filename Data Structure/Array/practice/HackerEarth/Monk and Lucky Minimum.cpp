/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Monk and Lucky Minimum
               Judge       :   HackerEarth
               Date        :   11/3/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int tc, n;
    cin >> tc;
    while(tc--) {
        cin >> n;
        long ar[n+1] = {0}, mn = INT_MAX, a;
        for(int i = 0; i < n; i++) {
            cin >> a;
            ar[a]++;
            mn = min(mn,a);
        }
        cout << ((ar[mn]%2 == 0)? "Unlucky" : "Lucky") << endl;
    }
    return 0;
}

/*

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int tc, n;
    scanf("%d",&tc);
    while(tc--) {
        scanf("%d",&n);
        int  mn = INT_MAX, a , lucky = 0;
        for(int i = 0; i < n; i++) {
            scanf("%d",&a);
            if(mn > a)
               mn = a, lucky = 0;
               if(mn == a) lucky++;
        }
        cout << ((lucky%2 == 0)? "Unlucky" : "Lucky") << endl;
    }
    return 0;
}
*/

