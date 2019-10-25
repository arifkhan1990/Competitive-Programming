/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 20: Sorting
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-sorting/problem
*/

#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    int numberOfSwaps = 0;
    cin >> n;
    vector<int> a(n);
    for(int a_i = 0;a_i < n;a_i++){
       cin >> a[a_i];
    }
    
    
    for (int i = 0; i < n; i++) {
    
    for (int j = 0; j < n - 1; j++) {
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
}
    cout<<"Array is sorted in "<<numberOfSwaps << " swaps."<<endl;
    cout<<"First Element: "<< a[0]<<endl<<"Last Element: "<<a[n-1]<<endl;
    return 0;
}