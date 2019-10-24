/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Unique Subarrays
               Judge       :   HackerEarth
               Date        :   12/3/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;

long long unsigned Sum(int ar[], int n)
{
    unordered_set<int>sp;
    long long unsigned j = 0, sum = 0;
    for(int i = 0; i < n; i++) {
        while(j < n and sp.find(ar[j]) == sp.end()) {
            sp.insert(ar[j]);
            j++;
        }
        sum += ((j-i)*(j-i+1))/2;
        sp.erase(ar[i]);
    }
    return sum;
}

int main()
{
    int n,m,a,tc;
    scanf("%d", &tc);
    while(tc--){
        scanf("%d", &n);
        int ar[n] = {0};
        for(int i = 0; i < n; i++) {
            scanf("%d",&ar[i]);
        }
        cout << Sum(ar,n) << endl;
    }

    return 0;
}
