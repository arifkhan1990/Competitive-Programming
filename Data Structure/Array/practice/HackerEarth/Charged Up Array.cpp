/*
             ...........................................................
               Solver      :   Arif Khan
               Problem     :   Charged Up Array
               Judge       :   HackerEarth
               Date        :   28/10/19
               Time        :   3.21291 Sec
               Memory      :   1308KB
               Difficulty  :   Easy
             ...........................................................
*/

#include<bits/stdc++.h>
using namespace std;
#define md  1000000007

int solve (vector<long long>& A) {
   long long subset = pow(2, A.size()-1), ans = 0;
   for(auto i: A){
   	if(i >= subset){
   		ans = (i+ans) % md;
   	}
   }
   return ans%md;
}

int main() {

    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for(int t_i=0; t_i<T; t_i++)
    {
        int N;
        cin >> N;
        vector<long long> A(N);
        for(int i_A=0; i_A<N; i_A++)
        {
        	cin >> A[i_A];
        }

        int out_;
        if(N < 64) out_ = solve(A);
        cout << ((N >= 64)? 0: out_ );
        cout << "\n";
    }
}