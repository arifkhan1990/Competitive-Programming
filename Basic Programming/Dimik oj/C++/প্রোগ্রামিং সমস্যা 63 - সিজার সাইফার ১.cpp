/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 63 - সিজার সাইফার ১
                      Difficulty: Easy
                      Time Complexity: 0.2034 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/63/caesar-cipher-1-by
*/

#include <bits/stdc++.h>
using namespace std;
#define ll long long int


int main() {
    int k;
    string s;
    getline(cin , s);
    cin >> k;
    for(int i = 0; i < s.size(); i++) {
        if(s[i] >= 'a' and s[i] <= 'z'){
            if(int(s[i])+k > int('z')) cout << char('a' - ('z' - int(s[i]) + 1) + k);
            else cout << char(s[i]+k);
        }else if(s[i] >= 'A' and s[i] <= 'Z'){
            if(int(s[i])+k > 'Z') cout << char('A' - ('Z' - int(s[i]) + 1) + k);
            else cout << char(s[i]+k);
        }else cout << s[i];
    }
    cout << endl;
	return 0;
}