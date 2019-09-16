#include <iostream>
using namespace std;

int main() {
	int tc, num;
	cin >> tc;
	while(tc--){
		cin >> num;
		cout << ((num&1)?"odd":"even") << endl;
	}
	return 0;
}