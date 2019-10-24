/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 7: Arrays
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-arrays/problem
*/

#include <vector>
#include <iostream>

using namespace std;


int main(){
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> arr[arr_i];
    }
      for(int arr_i = n-1;arr_i >=0;arr_i--){
       cout << arr[arr_i] <<" ";
    }
    return 0;
}