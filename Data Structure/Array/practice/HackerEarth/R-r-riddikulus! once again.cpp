/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   R-r-riddikulus! once again
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
   int n, k, a;
   cin >> n >> k;
   deque<int> ans;
   for(int i = 0; i < n; i++) {
    cin >> a;
    ans.push_back(a);
   }

   while(k--){
    ans.push_back(ans.front());
    ans.pop_front();
   }

   for(int i = 0; i < n ; i++) {
        cout << anas[i] << " ";
   }

   return 0;
}

/*
   int n, k, a;
   cin >> n >> k;
   int ar[n+1];
   for(int i = 0; i < n; i++) {
       cin >> a;
       if(i < k) ar[n-k+i] = a;
       else  ar[i-k] = a;
   }

   for(int i = 0; i < n ; i++) {
        cout << ar[i] << " ";
   }

*/
/*
 int ar[n], p = 1, p1 = step + 1;
    for(int i = 1; i <= n; i++) cin >> ar[i];
    while(n > 0) {
        if(n <= step) cout << ar[p++] << " ";
        if(n > step) cout << ar[p1++] << " ";
       n--;
    }

*/
