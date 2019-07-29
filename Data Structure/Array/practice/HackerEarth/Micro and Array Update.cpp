/*                    Name : Aziz Ahmed
                      Judge: HackerEarth
                      problem: Micro and Array Update
                      Difficulty: Very Easy
                      Problem Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/micro-and-array-update/
*/



#include <iostream>

using namespace std;

int main() {
	int T, N, K;
	
	cin >> T;
	
	for(int i = 0; i < T; i++){
	    cin >> N >> K;
	    int ans = 0, temp;
	    for(int j = 0; j < N; j++){
	        cin >> temp;
	        if(K-temp > ans) ans = K-temp;
	    }
	    cout << ans << endl;
	}
}
