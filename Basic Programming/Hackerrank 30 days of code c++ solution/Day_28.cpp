/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 28: RegEx, Patterns, and Intro to Databases
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-regex-patterns/problem
*/

#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;
    multiset<pair<string,string>>ms;
    multiset<pair<string,string>>::iterator it;
    for(int a0 = 0; a0 < N; a0++){
        string firstName;
        string emailID;
        string s;
        size_t p;
        cin >> firstName >> emailID;
        p = emailID.find('@');
        s = emailID.substr(p+1);
        ms.insert(make_pair(firstName,s));
    }
    for(it = ms.begin();it != ms.end(); it++){
        if(it->second == "gmail.com")
            cout<<it->first<<endl;
    }
    return 0;
}