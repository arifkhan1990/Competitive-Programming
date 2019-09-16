#include<bits/stdc++.h>
using namespace std;

int main()
{
    int tc;
    string s;
    scanf("%d ",&tc);
    while(tc--){
    	int ans = 0;
    	getline(cin, s);
    	stringstream line(s);
    	string num;
    	while (line >> num) {
    		ans++;
    	}
    	cout << ans << endl;
    }
    return 0;
}