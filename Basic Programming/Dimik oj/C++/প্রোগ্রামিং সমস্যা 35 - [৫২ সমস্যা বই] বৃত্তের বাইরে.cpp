/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 35 - [৫২ সমস্যা বই] বৃত্তের বাইরে
                      Difficulty: Easy
                      Time Complexity: 0.2277 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/35/out-of-the-circle-by
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
	cin >> n;
	while(n--) {
	    double  x1, y1, x2, y2, r, m;
		cin >> x1 >> y1 >> r >> x2 >> y2;
	    m = ((x2-x1)*(x2-x1))  +  ((y2-y1)*(y2-y1));
		double dis = sqrt(m);
		if(dis > r) {
		    cout << "The point is not inside the circle" << endl;
		}else{
		    cout << "The point is inside the circle" << endl;
		}
	}
	return 0;
}