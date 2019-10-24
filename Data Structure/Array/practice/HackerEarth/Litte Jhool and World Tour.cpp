/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Litte Jhool and World Tour
               Judge       :   HackerEarth
               Date        :   12/3/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;


int main()
{
    int tc, n ,m;
    scanf("%d",&tc);
    while(tc--) {
        //int a, b;
        scanf("%d %d",&n,&m);
        int b = 0;
        map<int,int>ans;
        for(int i = 0; i < m; i++) {
            int x, y;
            scanf("%d %d",&x,&y);
            if( x == y) {
                b = 1;
                break;
            }else if(x > n and x > y) {
                if( (x-y) > n ) b = 1;
            }
        }
        cout << ((b == 0)? "YES" :"NO") << endl;
    }
    return 0;
}
