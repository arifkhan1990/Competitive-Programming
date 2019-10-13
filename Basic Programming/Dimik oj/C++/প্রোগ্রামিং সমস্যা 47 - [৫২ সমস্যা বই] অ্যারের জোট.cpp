/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: পপ্রোগ্রামিং সমস্যা 47 - [৫২ সমস্যা বই] অ্যারের জোট
                      Difficulty: Easy
                      Time Complexity: 0.3059 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/47/array-affix-by
*/

#include <bits/stdc++.h>
using namespace std;
#define ll long long int


int main() {
    ll n, p , q, c;
	cin >> n;
	while(n--) {
	    vector<int> ans;
	    
       cin >> p;
       while(p--){
           cin >> q;
           ans.push_back(q);
       }
       
       cin >> p;
       while(p--){
           cin >> q;
           ans.push_back(q);
       }
       sort(ans.begin(), ans.end());
       for(int i = 0; i < ans.size(); i++){
           if(i != 0) cout << " ";
             cout << ans[i];
       }
    cout << endl;
	}
	return 0;
}