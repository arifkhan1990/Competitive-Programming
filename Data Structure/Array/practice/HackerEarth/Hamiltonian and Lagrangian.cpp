/*                    Name : Arif Khan
                      Judge: HackerEarth
                      problem: Hamiltonian and Lagrangian
                      Difficulty: Easy
                      Time Complexity: O(N^2)
                      Problem Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/hamiltonian-and-lagrangian/
*/


#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int ar[n+1];
    for(int i = 0; i < n; i++) cin >> ar[i];
    for(int i = 0; i < n; i++) {
        bool b = true;
        for(int j = i+1; j < n; j++){
           if(ar[i] < ar[j]) {
               b = false;
               break;
           }
        }
        if(b) cout << ar[i] << " ";
    }
    cout << endl;
    return 0;
}
