/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 18 - [৫২ সমস্যা বই] স্বরবর্ণ-ব্যাঞ্জনবর্ণ
                      Difficulty: Easy
                      Time Complexity: 0.2178 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/18/52-problem-book-vowels-and-consonants-by-dimik-computing
*/


#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    scanf("%d ",&t);
    for(int j = 0; j < t; j++) {
        string s, word = "", word2 = "";
        getline(cin, s);
        int ans = 0;
        for(int i = 0; i < s.size(); i++) {
        	if((s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z')) {
        		if(s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U')
        		        word += s[i];
        		else word2 += s[i];
        	}
        }
        cout << word << endl << word2 << endl;
    }
    return 0;
}