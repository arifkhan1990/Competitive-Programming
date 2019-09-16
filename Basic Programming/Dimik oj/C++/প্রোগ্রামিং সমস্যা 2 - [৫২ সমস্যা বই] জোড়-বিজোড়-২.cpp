#include <iostream>
using namespace std;
 
int main() {
	int tc;
	string s;
	cin >> tc;
	while(tc--) {
		cin >> s;
		cout << ((s[s.size()-1]%2)? "odd":"even") << endl;
	}
	return 0;
}