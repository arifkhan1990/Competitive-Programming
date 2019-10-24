/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 3: Intro to Conditional Statements
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-conditional-statements/problem
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n ;
    cin >> n ;
    if(((n>=2 && n<6) || n>20) && n%2==0)
        cout <<"Not Weird\n";
    else
        cout <<"Weird\n";
 return 0;
}