#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int tc,k;
    cin >> tc;
    for(int i = 1; i <= tc; i++) {
    	cin >> k;
    	for(int j = 1; j <= k; j++){
    		for(int p = 1; p <= k; p++){
    			cout <<"*";
    		}
    		cout << endl;
    	}
    	if(i != tc) cout << endl;
    }
	return 0;
}