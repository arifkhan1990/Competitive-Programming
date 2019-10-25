/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 29: Bitwise AND
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-bitwise-and/problem
*/

#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n, k,ans = 0,m = 0;
        cin >> n >> k;
        for(int i = 1; i<= n ;i++){
              for(int j = i+1; j<=n ;j++){
                ans = i & j;
                if(k > ans and m < ans)
                    m = ans;
            }
        }
        cout<<m<<endl;
    }
    return 0;
}