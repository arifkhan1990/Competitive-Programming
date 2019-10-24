/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Perfect Subarray
               Judge       :   HackerEarth
               Date        :   14/3/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/


#include<bits/stdc++.h>
using namespace std;

bool sqt(int sum) {
    int a = 0;double b = 0;
    b = sqrt(sum);
    a = b;
    if(a == b) return true;

    return false;
}

int main()
{
    int n;
    scanf("%d",&n);
    int ar[n+1], ans = 0;
    for(int i = 0; i < n; i++) scanf("%d",&ar[i]);
    vector<int> res;
    for(int i = 0; i < n; i++) {
        if(i != 0) {
            for(int j = 0, sz = res.size(); j < sz; j++) {
                res[j] += ar[i];
                if(sqt(res[j])) ans++;
            }
            if(sqt(ar[i] + ar[i-1])) ans++;
            res.push_back(ar[i]+ar[i-1]);
        }
        if(sqt(ar[i])) ans++;
       }
    printf("%d\n",ans);
    return 0;
}
