/*                    Name : Arif Khan , Asif Khan, Ripon Ahammed , Munna, Subho, Hossain Ahammed
                      Judge: HackerRank
                      problem: Maps-STL
                      Difficulty: Easy
                      Time Complexity: O(logN)
                      Problem Link: https://www.hackerrank.com/challenges/cpp-maps/problem
*/

#include <iostream>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    ios::sync_with_stdio(false);cin.tie(0);
    int noOfQuery, queryType, studentMark;
    string studentName;

    map<string, int> mp;

    cin >> noOfQuery;
    while(noOfQuery--) {
        cin >> queryType;
        map<string, int>::iterator it = mp.begin();
        if(queryType == 1) {
            cin >> studentName >> studentMark;
            if(!mp.count(studentName)) {
                mp.insert(make_pair(studentName,studentMark));
            }else {
                mp[studentName] += studentMark;
            }
        }else if(queryType == 2) {
            cin >> studentName;
            mp.erase(studentName);
        }else {
            cin >> studentName;
            auto val = mp.find(studentName);
            cout << (mp.count(studentName)? val->second : 0 ) << endl;
        }
    }

    return 0;
}
