/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 14: Scope
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-scope/problem
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Difference {
    private:
    vector<int> elements;
  
  	public:
  	int maximumDifference;
	
    Difference (vector<int>inArray) :maximumDifference(0)
    {
        this->elements  = inArray;
    }

    void computeDifference () {
        int l_v = 101;
        int h_v = 0;
        for(int i = 0; i<elements.size() ;i++){
            l_v = min(l_v,elements[i]);
            h_v = max(h_v,elements[i]);
        }

        maximumDifference = (h_v - l_v);
}

};

int main() {
    int N;
    cin >> N;
    
    vector<int> a;
    
    for (int i = 0; i < N; i++) {
        int e;
        cin >> e;
        a.push_back(e);
    }
    
    Difference d(a);
    d.computeDifference();
    
    cout << d.maximumDifference;
    return 0;
}