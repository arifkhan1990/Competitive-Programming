/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Achhe Din
               Judge       :   HackerEarth
               Date        :   15/3/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;

int main()
{
   int tc, n, a;
   scanf("%d",&tc);

   while(tc--) {
    scanf("%d",&n);
    map<int, int>data;
    map<int, int>::iterator it;

    for(int i = 0; i < n ; i++) {
        scanf("%d",&a);
        data[a]++;
    }
    for(it = data.begin(); it != data.end(); it++) {
        if(it->second == 1) {
            printf("%d\n", it->first);
            break;
        }
    }
   }

   return 0;
}

