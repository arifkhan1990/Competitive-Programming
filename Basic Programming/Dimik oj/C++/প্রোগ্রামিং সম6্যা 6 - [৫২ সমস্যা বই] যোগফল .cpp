#include<iostream>
using namespace std;

int main()
{
    int tc;
    string s;
    cin >> tc;
    while(tc--){
        cin >> s;
        cout << "Sum = " << s[0]-'0' + s[4]-'0' << endl;
    }
    return 0;
}