/*                    Name : Arif Khan
                      Judge: UVA
                      problem: Digit Generator
                      Difficulty: Medium
                      Time Complexity: O(N*M) (0.080s)
                      Problem Link: https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4458
*/

#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int n, k;
    cin >> n;
    while(n--) {
        cin >> k;
        int ans = 0, res = 0;
        int range = (k < 10) ? 9 : (k < 100)? 18: (k < 1000)? 27: (k < 10000)? 45 : 60;
        for(int i = k - range; i <= k; i++) {
            int num = i, sum = i;
            while( num != 0) {
                sum += num%10;
                num /= 10;
            }
            if(sum == k) {
                ans = 1;
                res = i;
                break;
            }
        }
        cout << ((ans)? res : 0 ) << endl;
    }
    return 0;
}
