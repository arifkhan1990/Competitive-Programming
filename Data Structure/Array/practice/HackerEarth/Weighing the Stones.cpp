/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Weighing the Stones
               Judge       :   HackerEarth
               Date        :   16/3/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;

int main()
{
   int tc, n , a;
   scanf("%d",&tc);
   while(tc--) {
    scanf("%d",&n);
    map<int, int>rupam , ankit;
    map<int, int>::iterator it;
    int rupamIdx, ankitIdx, rupamMx = 0, ankitMx = 0;
    for(int i = 0; i < n; i++) {scanf("%d",&a);rupam[a]++;}
    for(int i = 0; i < n ; i++) {scanf("%d",&a);ankit[a]++;}

    for(it = rupam.begin(); it != rupam.end(); it++) {
        if(rupamMx <= it->second) {
            rupamMx = it->second;
            rupamIdx = it->first;
        }
    }
    for(it = ankit.begin(); it != ankit.end(); it++) {
        if(ankitMx <= it->second) {
            ankitMx = it->second;
            ankitIdx = it->first;
        }
    }
    cout << (rupamIdx == ankitIdx? "Tie\n": rupamIdx < ankitIdx ? "Ankit\n": "Rupam\n");
   }

   return 0;
}
