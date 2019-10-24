/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Pepper and Contiguous Even Subarray
               Judge       :   HackerEarth
               Date        :   19/3/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define likeC ios::sync_with_stdio(0); cin.tie(0);cout.tie(0);

int main()
{
    likeC;
    int n, p,k;
    multiset<int>ar;
    cin >> k >> n;
      int arr[n+1];
      for(int i = 0; i < n; i++) cin >> arr[i];
    for(int i = 0; i < n; i++) {
            p = arr[i];

            multiset<int>::iterator it = ar.upper_bound(p-k);
            if(it == ar.end()) ar.insert(p);
            if( *it > p) {
            	ar.erase(it);
            	ar.insert(p);
            }
    }
    printf("%d\n", ar.size());

    return 0;
}
