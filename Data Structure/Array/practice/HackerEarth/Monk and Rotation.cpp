/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Monk and Rotation
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
    int n, k, tc;
    scanf("%d",&tc);
    while(tc--) {
        scanf("%d %d",&n,&k);
        int a;
        deque<int>ans;

        for(int i = 0; i < n; i++) {
            scanf("%d",&a);
            ans.push_back(a);
        }

        for(int i = 0; i < k; i++) {
         ans.push_front(ans.back());
         ans.pop_back();
        }

        deque <int> :: iterator it;
        for (it = ans.begin(); it != ans.end(); ++it)
            cout  << *it << " ";
    }

    return 0;
}
