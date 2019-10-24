/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 9: Recursion 3
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-recursion/problem
*/


#include <bits/stdc++.h>
using namespace std;

int factorial(int n);
int main() {
    int n1,r;
    cin >> n1;
    r = factorial(n1);
    cout << r <<endl;
    return 0;
}
int factorial(int n){
    if(n<=1)
        return 1;
    else 
        return n*factorial(n-1);
}