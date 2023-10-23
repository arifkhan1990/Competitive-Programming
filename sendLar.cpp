#include<bits/stdc++.h>
using namespace std;

int main()
{
    int fmx = 0, smx = 0, fmn = INT_MAX, smn = INT_MAX, n, data;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> data;

        if(fmx < data){
            smx = fmx;
            fmx = data;
        }else if(smx < data){
            smx = data;
        }

        if(fmn > data){
            smn = fmn;
            fmn = data;
        }else if(smn > data){
            smn = data;
        }

        cout << "1st Maximum: " << fmx << endl << "2nd Maximum: " << smx << endl;
        cout << "1st Minimum: " << fmn << endl << "2nd Minimum: " << smn << endl;
    }

    cout << "1st Maximum: " << fmx << endl << "2nd Maximum: " << smx << endl;
    cout << "1st Minimum: " << fmn << endl << "2nd Minimum: " << smn << endl;

    return 0;
}