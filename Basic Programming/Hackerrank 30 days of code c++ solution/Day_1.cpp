/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 1: Data Types
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-data-types/problem
*/

#include <iostream>
using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";
    int n;
    double n1;
 
    cin >> n >> n1;
    char s1[1000];
    cin.getline(s1,0);
    cin.getline(s1,1000);
    cout <<i+n<<"\n";
    cout<<fixed<<setprecision(1)<<d+n1<<endl;
    cout<<s<<s1<<endl;
    return 0;
}