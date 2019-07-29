/*                    Name : Arif Khan
                      Judge: HackerRank
                      problem: Arrays - DS
                      Difficulty: Easy
                      Time Complexity: O(N)
                      Problem Link: https://www.hackerrank.com/challenges/arrays-ds/submissions/code/32433403
*/


#include <bits/stdc++.h>
using namespace std;


int main(){
    int n;
    cin >> n;
    //vector<int> arr(n);
    int arr[n];
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> arr[arr_i];
    }
        for(int arr_i = n-1;arr_i >=0;arr_i--){
         cout << arr[arr_i] << " ";
    }
    return 0;
}
