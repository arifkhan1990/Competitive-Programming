/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 17 - [৫২ সমস্যা বই] স্বরবর্ণ গণনা
                      Difficulty: Easy
                      Time Complexity: 0.1917 সেকেন্ড
                      Problem Link:https://dimikoj.com/problems/17/52-problem-book-counting-vowels-by-dimik-computing
*/

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    scanf("%d ",&t);
    char v[5] = {'a','e','i','o','u'};
    for(int i = 0; i < t; i++) {
        string s;
        getline(cin, s);
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        int ans = 0;
        for(int i = 0; i < 5; i++) {
            ans += count(s.begin(), s.end(),v[i]);
        }
        cout << "Number of vowels = " << ans << endl;
    }
    return 0;
}