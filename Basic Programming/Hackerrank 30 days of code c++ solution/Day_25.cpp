/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 25: Running Time and Complexity
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool primech(int n){
    for(int i = 2; i<= sqrt(n) ;i++){
        if(n%i == 0)
            return false;
    }
    return true;
}

int main() {
    int n;
    cin>>n;
    while(n--){
        long t;
        cin >> t;
        if(primech(t) and t>=2) cout<<"Prime"<<endl;
            else cout<<"Not prime"<<endl;
    }
    return 0;
}