/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 2: Operators
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-operators/problem
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    double p , tax ,tip,result;
    int meal,t;
    cin >> p >> meal >> t;
    tip = (p *meal)/100;
    tax = (p *t)/100 ;
    result = p + tip + tax ;
 
     if(result<(int)result+.45)
     cout << "The total meal cost is "<<(int)result <<" dollars.\n";
     else
     cout << "The total meal cost is "<<(int)result+1 <<" dollars.\n";
    return 0;
}