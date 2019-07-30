/*                    Name : Arif Khan
                      Judge: HackerRank
                      problem: Vector-Sort
                      Difficulty: Easy
                      Time Complexity: O(N)
                      Problem Link: https://www.hackerrank.com/challenges/arrays-ds/submissions/code/32433403
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    vector<long>ans;
    cin>>n;
    for(int i = 0 ;i<n ;i++){
        int k ;
        cin >> k;
        ans.push_back(k);
    }
    sort(ans.begin(),ans.end());
    for(int i = 0; i<n ;i++)
        cout<<ans[i]<<" ";
    return 0;
}
