/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Biased Chandan
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
   int n , a, sum = 0;
   scanf("%d",&n);
   deque<int> ans;
   while(n--) {
    scanf("%d",&a);

    a>0 ? ans.push_back(a):ans.pop_back();
   }
   for(int i = 0; i < ans.size(); i++) sum += ans[i];
   printf("%d\n", sum);
   return 0;
}

