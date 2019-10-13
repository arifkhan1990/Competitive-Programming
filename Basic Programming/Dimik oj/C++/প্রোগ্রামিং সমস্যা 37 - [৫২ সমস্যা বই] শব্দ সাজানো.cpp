/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 37 - [৫২ সমস্যা বই] শব্দ সাজানো
                      Difficulty: Easy
                      Time Complexity: 0.2485 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/37/word-sorting-by
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    set<string> st;
	cin >> n;
	while(n--) {
	    string s;
	    cin >> s;
	    st.insert(s);
	}
	for(auto it = st.begin(); it != st.end(); it++) {
	    cout << *it << endl;
	}
	return 0;
}