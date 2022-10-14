#include<bits/stdc++.h>
using namespace std;

long long binPow(long long a, long long b)
{
    long long res = 1;
    while(b > 0) {
        if (b&1)
            res = res*a;
        a = a*a;
        b >>= 1;
    }
    return res;
}

int main()
{
    long long a, b;
    cin >> a >> b;
    cout << binPow(a,b) << endl;
    return 0;
}