/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 19 - [৫২ সমস্যা বই] শব্দ গণনা -১
                      Difficulty: Easy
                      Time Complexity: 0.4863 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/19/52-problem-book-counting-words-1-by-dimik-computing
*/


#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    scanf("%d ",&t);
    for(int j = 0; j < t; j++) {
        string s, word = "";
        getline(cin, s);
        stringstream st(s);
        int ans = 0;
        while(st >> word) ans++;
        cout << "Count = " << ans << endl;
    }
    return 0;
}