/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 64 - সিজার সাইফার ২
                      Difficulty: Easy
                      Time Complexity: 0.2485 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/64/caesar-cipher-2-by
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
            if(int(s[i])-k < 97) cout << char('z' + (int(s[i] - 'a' + 1) - k));
            else cout << char(s[i]-k);
        }else if(s[i] >= 'A' and s[i] <= 'Z'){
            if(int(s[i])-k < 65) cout << char('Z' + (int(s[i] - 'A' + 1) - k));
            else cout << char(s[i]-k);
        }else cout << s[i];
    }
    cout << endl;
	return 0;
}