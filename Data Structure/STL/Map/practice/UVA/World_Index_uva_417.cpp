/*                    Name : Arif Khan , Asif Khan, Ripon Ahammed , Munna, Subho, Hossain Ahammed
                      Judge: UVA
                      problem: 417 Word Index
                      Difficulty: Easy
                      Time Complexity: O(N*26*26*26*26*26)
                      Problem Link: https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=358
*/
#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int n = 0, m = 26, k = 0;
    string s, st="abcdefjhijklmnopqrstuvwxyz";
    map<string, int> mp;
    for(int i = 0 ; i < 26;i++) {
            s = st[i];
            mp.insert(make_pair(s,++k));
    }

    for(int i = 0 ; i < 26; i++) {
        s  = st[i];
        for(int j = i+1; j < 26; j++) {
             s += st[j];
            mp.insert(make_pair(s,++k));
            s = st[i];
        }
        s = "";
    }

   s = "";

   for(int i = 0 ; i < 26; i++) {
        s  = st[i];
    for(int j = i+1; j < 26; j++) {
         s += st[j];
        for(int p = j+1; p < 26; p++) {
            s += st[p];
            mp.insert(make_pair(s, ++k));
            s = "";
            s += st[i];
            s += st[j];
        }
        s = "";
        s = st[i];
    }
    s = "";
   }

 for(int i = 0 ; i < 26; i++) {
        s  = st[i];
    for(int j = i+1; j < 26; j++) {
         s += st[j];
        for(int p = j+1; p < 26; p++) {
            s += st[p];
            for(int q = p+1; q < 26; q++) {
                    s += st[q];
            mp.insert(make_pair(s, ++k));
            s = "";
            s += st[i];
            s += st[j];
            s += st[p];
            }
            s = "";
            s += st[i];
            s += st[j];
        }
        s = "";
        s = st[i];
    }
    s = "";
   }

    for(int i = 0 ; i < 26; i++) {
        s  = st[i];
    for(int j = i+1; j < 26; j++) {
         s += st[j];
        for(int p = j+1; p < 26; p++) {
            s += st[p];
            for(int q = p+1; q < 26; q++) {
                    s += st[q];
                for(int r = q+1; r < 26; r++) {
                        s += st[r];
            mp.insert(make_pair(s, ++k));
            s = "";
            s += st[i];
            s += st[j];
            s += st[p];
            s += st[q];
                }
            s = "";
            s += st[i];
            s += st[j];
            s += st[p];
            }
            s = "";
            s += st[i];
            s += st[j];
        }
        s = "";
        s = st[i];
    }
    s = "";
   }

   //for(auto it = mp.begin(); it != mp.end(); it++) cout << it->first << " " << it->second << endl;
    while(cin >> s){
    map<string, int>::iterator it = mp.find(s);
    cout << ( (mp.count(s))? it->second: 0) << endl;
    }
    return 0;
}
