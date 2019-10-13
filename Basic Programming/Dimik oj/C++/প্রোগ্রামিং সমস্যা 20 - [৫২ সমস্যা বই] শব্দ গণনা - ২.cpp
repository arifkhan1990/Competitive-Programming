/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 20 - [৫২ সমস্যা বই] শব্দ গণনা - ২
                      Difficulty: Easy
                      Time Complexity: 0.2293 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/20/52-problem-book-counting-words-2-by-dimik-computing
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