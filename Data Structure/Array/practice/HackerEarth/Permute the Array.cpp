/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Permute the Array
               Judge       :   HackerEarth
               Date        :   17/3/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;

map<int, int> Arr;
map<int,int>::iterator it;

bool Check_Subarray (int N, int K) {
   if( N == K) return true;
   int len = Arr.size();
   if(len > K) return false;
   int p = floor(N/K);
   for(it = Arr.begin(); it != Arr.end(); it++)
       if(it->second  < p) return false;

    return true;
}

int main() {

    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for(int t_i=0; t_i<T; t_i++)
    {
        int N, a;
        cin >> N;
        int K;
        cin >> K;
        for(int i_Arr=0; i_Arr<N; i_Arr++)
        {
        	cin >> a;
        	Arr[a]++;
        }
        bool out_;
        out_ = Check_Subarray(N, K);
        if(out_) cout<<"YES\n";
        else cout<<"NO\n";
    }
}
