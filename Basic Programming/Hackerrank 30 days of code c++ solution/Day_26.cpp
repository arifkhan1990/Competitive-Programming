/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 26: Nested Logic
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-nested-logic/problem
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
   int d1,m1,y1,d2,m2,y2;
    cin>>d1>>m1>>y1>>d2>>m2>>y2;
    if(y1>y2) return cout<<10000, 0;
    else if(y1 == y2){ 
        if(m1>m2) return cout<<(m1-m2)*500,  0;
        else if(m1 == m2 and d1 > d2) return cout<<(d1-d2)*15, 0;
    }
    cout<<0<<endl;
    return 0;
}