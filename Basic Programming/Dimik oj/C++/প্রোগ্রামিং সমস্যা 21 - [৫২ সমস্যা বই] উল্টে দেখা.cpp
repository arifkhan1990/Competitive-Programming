/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 21 - [৫২ সমস্যা বই] উল্টে দেখা
                      Difficulty: Easy
                      Time Complexity: 0.3253 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/21/reverse-show-by
*/

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    scanf("%d ",&t);
    for(int j = 0; j < t; j++) {
        string s;
        getline(cin, s);
        reverse(s.begin(), s.end());
        cout << s << endl;
    }
    return 0;
}