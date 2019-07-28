#include <iostream>
using namespace std;

int main()
{
    // Array declaration and initialization
    int arr[5] = {4, 12, 7, 15, 9};
    // Iterate over the array
    for(int idx=0; idx<5; idx++)
    {
        // Print out each element in a new line
        cout << "arr[" << idx << "] = " << arr[idx] << endl;
    }
    return 0;
}
