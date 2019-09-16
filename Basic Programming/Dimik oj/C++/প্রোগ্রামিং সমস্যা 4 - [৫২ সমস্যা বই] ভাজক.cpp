#include <bits/stdc++.h>
using namespace std;

int main() {
    int tc,k;
    cin >> tc;
    for(int i = 1; i <= tc; i++) {
    	cin >> k;
    	cout << "Case " << i << ": ";
    	for(int j = 1; j <= k/2; j++){
    		if(k%j == 0) cout << j << " ";
    	}
    	cout << k << endl;
    }
	return 0;
}