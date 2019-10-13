/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 23 - [৫২ সমস্যা বই] বর্ণমালা থেকে সংখ্যা
                      Difficulty: Easy
                      Time Complexity: 0.3180 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/23/alphabet-to-number-by
*/

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t, a, b;
    scanf("%d ",&t);
    for(int j = 0; j < t; j++) {
    	string s;
    	cin >> s;

    	for(int i = 0, sz = s.size(); i < sz; i++) {
    		cout << (s[i]-'A')+1;
    	}
    	cout << endl;
    }
    return 0;
}