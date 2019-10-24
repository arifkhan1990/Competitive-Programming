/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   SnackDown Contest
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
    int n, p, q, po;
    cin >> n;

    for(int i = 0; i < n; i++) {
        scanf("%d %d",&po,&p);

        int ar[po+1] = {0};
        while(p--) {
            scanf("%d",&q);
            ar[q]++;
        }
        scanf("%d",&p);
        while(p--) {
            scanf("%d",&q);
            ar[q]++;
        }
        int b = 1;
        for(int j = 1; j <= po; j++) {
            if(ar[j] == 0){
                b = 0;
                break;
            }
        }
        cout << ((b)? "YES": "NO") << endl;
    }
    return 0;
}
