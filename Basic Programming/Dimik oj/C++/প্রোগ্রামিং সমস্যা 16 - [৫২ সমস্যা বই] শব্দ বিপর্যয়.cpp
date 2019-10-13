/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 16 - [৫২ সমস্যা বই] শব্দ বিপর্যয়
                      Difficulty: Easy
                      Time Complexity: 0.1291 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/16/52-problem-book-reverse-words-by-dimik-computing
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	scanf("%d ",&t);
	
	while(t--) {
		string s;
		vector<string> ans;
		getline(cin, s);
		stringstream str(s);
		string word;
		
		while(str >> word) {
			ans.push_back(word);
		}
		
		for(int i = 0; i < ans.size(); i++) {
			string single = ans[i];
			reverse(single.begin(),single.end());
			cout << single;
			if(i < ans.size() - 1) cout << " ";
		}
		if(t >= 0)cout << endl;
	}
	return 0;
}