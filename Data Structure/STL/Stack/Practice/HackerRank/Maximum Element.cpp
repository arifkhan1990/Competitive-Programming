/*                    Name : Arif Khan
                      Judge: HackerRank
                      problem: Maximum Element
                      Difficulty: Easy
                      Time Complexity: O(N)
                      Problem Link: https://www.hackerrank.com/challenges/maximum-element/problem
*/
#include <bits/stdc++.h>
using namespace std;


int main() {
    int n, typeInput, data;
    cin >> n;
    stack<int>main,copy;

    while(n--) {
        cin >> typeInput;

        if(typeInput == 1) {
            cin >> data;
            main.push(data);

            if(main.size() == 1) copy.push(data);
            else if(data > copy.top()) copy.push(data);
            else copy.push(copy.top());
        }else if(typeInput == 2 and !main.empty()) {
            main.pop();
            copy.pop();
        }else {
            cout << copy.top() << endl;
        }
    }
    return 0;
}

