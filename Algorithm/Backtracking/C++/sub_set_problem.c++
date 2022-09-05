#include <bits/stdc++.h>
using namespace std;

vector<vector<int> >subsets(vector<int>& nums) {
    if (nums.empty()) return {{}};

    int n = nums.back();
    nums.pop_back();

    vector<vector<int>> res = subsets(nums);

    int size = res.size();
    cout << n << " = " << size << endl;
    for (int i = 0; i < size; i++) {
        res.push_back(res[i]);
        res.back().push_back(n);
    }
    for(int i = 0; i < res.size(); i++) {
        cout << "[ ";
        for(int j = 0; j <res[i].size(); j++) {
            cout << res[i][j] << ' ';
        }
       cout << " ]" << endl;
    }
    cout << endl;
    return res;
}

int main(){
    vector<int> nums{ 1, 2, 3 };
    vector<vector<int>> res = subsets(nums);
    cout << res.size() << endl;


    
    return 0;
}