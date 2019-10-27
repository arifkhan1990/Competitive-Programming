    /*
                 ...........................................................
                   Solver      :   Arif Khan
                   Problem     :   Pairs Having Similar Elements
                   Judge       :   HackerEarth
                   Date        :   27/10/19
                   Time        :   1.84665Sec
                   Memory      :   8224KB
                   Difficulty  :   Easy
                 ...........................................................
    */
#include<bits/stdc++.h>
using namespace std;

long long SimilarElementsPairs(vector<int> A, int N)
{
    sort(A.begin(),A.end());
    long long int ans = 0;

    for(int i = 1; i < N; i++) {
        long long int cnt = 1, st = 1;
        while((A[i] == A[i-1]) or (A[i] == A[i-1]+1)){
            st++;
            if(A[i] == A[i-1]) cnt++;
            i++;
        }
        if(st != 1 and st != cnt) ans += (st*(st-1))/2;
    }
    return  ans;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    vector<int> A(N);
    for(int i_A=0; i_A<N; i_A++)
    {
    	cin >> A[i_A];
    }
 
    long long out_;
    out_ = SimilarElementsPairs(A,N);
    cout << out_;
    return 0;
}